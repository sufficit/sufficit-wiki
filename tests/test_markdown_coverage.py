"""Repository documentation hierarchy and the behavior of its checker."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / f'scripts/{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


coverage = load('markdown_coverage')
Graph = coverage.MarkdownGraph


class RepositoryTests(unittest.TestCase):
    def test_every_markdown_file_is_in_the_hierarchy(self):
        self.assertEqual(coverage.check(ROOT), [])



class GraphTests(unittest.TestCase):
    def test_reports_orphans_and_disconnected_cycles(self):
        graph = Graph({'README.md': '[Guide](guide.md)', 'guide.md': '[Root](README.md)',
                       'orphan.md': '[Self](orphan.md)', 'cycle-a.md': '[B](cycle-b.md)', 'cycle-b.md': '[A](cycle-a.md)'})
        self.assertEqual(graph.unreachable(), ['cycle-a.md', 'cycle-b.md', 'orphan.md'])

    def test_follows_relative_root_encoded_reference_and_html_links(self):
        graph = Graph({'README.md': '[Guide](docs/) [Other][other]\n\n[other]: /OTHER.MD#section\n', 'OTHER.MD': '',
                       'docs/README.md': '[Details](./nested/../a%20b.md?view=1#section)',
                       'docs/a b.md': '<p>See <a href="../end.md">End</a></p>\n', 'end.md': ''})
        self.assertEqual(graph.unreachable(), [])

    def test_ignores_code_images_comments_and_plain_mentions(self):
        content = ('plain.md\n`[Code](inline.md)`\n![Image](image.md)\n'
                   '<!-- [Hidden](comment.md) <a href="comment.md">Hidden</a> -->\n\n'
                   '```markdown\n[Example](fenced.md)\n```\n\n    [Indented](indented.md)\n\n'
                   '<pre><a href="pre.md">Example</a></pre>\n')
        targets = ['comment.md', 'fenced.md', 'image.md', 'indented.md', 'inline.md', 'plain.md', 'pre.md']
        graph = Graph({'README.md': content, **{target: '' for target in targets}})
        self.assertEqual(graph.unreachable(), targets)

    def test_ignores_external_links_anchors_and_paths_outside_repository(self):
        graph = Graph({'README.md': '[Web](https://example.com/remote.md) [Relative web](//example.com/remote.md) '
                                    '[Mail](mailto:remote.md) [File](file:///remote.md) [Anchor](#remote.md) '
                                    '[Outside](../remote.md) [Encoded outside](%2E%2E/remote.md) [Py](script.py)',
                       'remote.md': ''})
        self.assertEqual(graph.unreachable(), ['remote.md'])
        self.assertEqual(graph.missing_targets(['README.md']), {})

    def test_reports_missing_targets_only_for_requested_sources(self):
        graph = Graph({'README.md': '[Index](docs/README.md)',
                       'docs/README.md': '[Deleted](deleted.md) [Renamed](old%20name.md#intro)',
                       'history.md': '[Old evidence](obsolete.md)'})
        self.assertEqual(graph.missing_targets(['README.md', 'docs/README.md']),
                         {'docs/README.md': ['docs/deleted.md', 'docs/old name.md']})


class ExemptionTests(unittest.TestCase):
    def test_directory_prefixes_and_segment_globs(self):
        exempt = coverage.Exemptions(['docs/activities/', '/AGENTS.md', 'Sufficit/*/NOTES.md'])
        self.assertEqual(exempt.filter(['AGENTS.md', 'docs/AGENTS.md', 'docs/activities/2026-x.md', 'docs/activitiesX.md',
                                        'Sufficit/a/NOTES.md', 'Sufficit/a/b/NOTES.md']),
                         ['docs/AGENTS.md', 'docs/activitiesX.md', 'Sufficit/a/b/NOTES.md'])

    def test_ignore_file_skips_comments_and_blank_lines(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / coverage.IGNORE_FILE).write_text('# comment\n\ndocs/activities/\n')
            exempt = coverage.Exemptions.load(root)
        self.assertEqual(exempt.filter(['docs/activities/z.md', 'docs/z.md']), ['docs/z.md'])

    def test_site_exclusions_come_from_jekyll_config(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / '_config.yml').write_text('title: x\nexclude:\n  - docs\n  - "AGENTS.md"\ndefaults:\n  - scope:\n')
            unpublished = coverage.site_exclusions(root)
        self.assertEqual(unpublished.filter(['docs/a.md', 'AGENTS.md', 'README.md', 'Sufficit/Sales/index.md',
                                             '_drafts/x.md', '.github/x.md', 'docsX.md']),
                         ['README.md', 'Sufficit/Sales/index.md', 'docsX.md'])


class WikiLinkTests(unittest.TestCase):
    def test_directory_links_resolve_to_index_or_readme(self):
        graph = Graph({'README.md': '[Sales](Sufficit/Sales/) [Gateway](Sufficit/Gateway)',
                       'Sufficit/Sales/index.md': '', 'Sufficit/Gateway/README.md': ''})
        self.assertEqual(graph.unreachable(), [])

    def test_github_links_to_this_repository_count_as_local(self):
        graph = Graph({'README.md': '[Agents](https://github.com/sufficit/sufficit-wiki/blob/main/AGENTS.md) '
                                    '[Other repo](https://github.com/sufficit/other/blob/main/x.md)',
                       'AGENTS.md': '[Plan](docs/PLAN-X.md)', 'docs/PLAN-X.md': '', 'x.md': ''})
        self.assertEqual(graph.unreachable(), ['x.md'])

    def test_published_page_must_not_link_relatively_to_unpublished_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(['git', 'init', '--quiet'], cwd=root, check=True)
            (root / '_config.yml').write_text('exclude:\n  - docs\n  - AGENTS.md\n')
            (root / 'README.md').write_text('[Agents](AGENTS.md) [Page](page.md)')
            (root / 'page.md').write_text('[Agents](https://github.com/sufficit/sufficit-wiki/blob/main/AGENTS.md)')
            (root / 'AGENTS.md').write_text('[Plan](docs/plan.md)')
            (root / 'docs').mkdir()
            (root / 'docs/plan.md').write_text('')
            errors = coverage.check(root)
        self.assertEqual(len(errors), 1)
        self.assertIn('README.md -> AGENTS.md', errors[0])
        self.assertNotIn('page.md', errors[0])
        self.assertNotIn('docs/plan.md', errors[0])


class InventoryTests(unittest.TestCase):
    def test_uses_tracked_and_new_files_excluding_ignored_and_deleted(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            git = lambda *args: subprocess.run(['git', *args], cwd=root, check=True, capture_output=True)
            git('init', '--quiet')
            (root / '.gitignore').write_text('ignored.md\n')
            (root / 'README.md').write_text('[New](new.md)')
            (root / 'deleted.md').write_text('')
            git('add', 'README.md', 'deleted.md')
            (root / 'deleted.md').unlink()
            for name in ('new.md', 'ignored.md', 'other.txt'):
                (root / name).write_text('')
            graph = Graph.from_repository(root)
        self.assertEqual(graph.paths(), ['README.md', 'new.md'])
        self.assertEqual(graph.unreachable(), [])

    def test_fails_explicitly_outside_git(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(RuntimeError, 'cannot inventory documentation'):
                Graph.from_repository(Path(temp))


if __name__ == '__main__':
    unittest.main()
