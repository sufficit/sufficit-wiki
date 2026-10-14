# Publicação da wiki no GitHub Pages

Publicada a documentação de alertas de monitoramento no commit `d91d429`, na branch `main`. GitHub Pages habilitado para a raiz dessa branch, com domínio `wiki.sufficit.com.br`.

Configuração Jekyll com tema padrão Primer e conversão de links Markdown para HTML. Índice raiz gerado a partir do README. Planos, atividades e instruções de agentes foram excluídos do site renderizado, permanecendo no repositório público.

## Evidência

- [Build e deploy](https://github.com/sufficit/sufficit-wiki/actions/runs/38615090821): concluídos com sucesso.
- API Pages confirmou estado `built` e domínio configurado.
- Artefato gerado conferido: página inicial, página de alertas, conversão dos links e exclusão dos documentos de manutenção.
- `git diff --check` passou antes da publicação.

## DNS e HTTPS

Na consulta realizada durante a entrega, o domínio ainda não retornava registro A ou CNAME. O responsável pelo DNS deve criar `wiki CNAME sufficit.github.io`, sem caminho de repositório. A configuração no provedor não foi alterada nesta atividade.

Após a propagação e emissão do certificado pelo GitHub, ativar **Enforce HTTPS** nas configurações de Pages. Na entrega, o certificado ainda não estava disponível e HTTPS obrigatório permanecia desativado.

[Orientação oficial para domínio personalizado](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

Acesso imediato à documentação: [arquivo público no GitHub](https://github.com/sufficit/sufficit-wiki/blob/main/Sufficit/Gateway/Zabbix/alertas-monitoramento.md). O domínio personalizado depende do DNS.

Plano concluído e removido; nenhuma alteração em serviços de telefonia ou contas de clientes.
