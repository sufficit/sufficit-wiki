---
title: Genius | GitHub CLI e Radicle
permalink: /ai/genius/toolchain/
redirect_from:
  - /Genius/toolchain/
---

# Genius — GitHub CLI e Radicle

Namespace `Sufficit.AI.Genius`.

Use o GitHub CLI (`gh`) para consultar repositórios, issues e pull requests do GitHub. Use o Radicle (`rad`) para trabalhar com repositórios da rede Radicle. O Genius oferece os dois como plugins no catálogo. Este manual mostra como instalar os plugins, escolher onde os comandos rodam, verificar a instalação e retirar permissões.

- [Instalar os plugins](#instalar-os-plugins)
- [Usar no Linux](#usar-no-linux)
- [Usar no Android](#usar-no-android)
- [Verificar os comandos](#verificar-os-comandos)
- [Revogar, desativar ou remover](#revogar-desativar-ou-remover)
- [Resolver problemas](#resolver-problemas)

## Onde os comandos rodam

| Onde você abre o Genius | Onde `gh` e `rad` rodam | O que você precisa |
| --- | --- | --- |
| Desktop Linux x86-64 | No próprio computador, pelo shell do Genius. | Sessão local e plugins ativos. |
| Android | Em um executor Linux na nuvem. Um executor é o computador remoto que roda as ferramentas da conversa. | Sessão criada na nuvem, em um executor próprio compatível com os plugins e autorizado na sua conta Sufficit. |
| Outro dispositivo conectado | No dispositivo exibido na conversa, conforme as ferramentas que ele oferece. | Confira o ambiente indicado em **Dispositivo da sessão** antes de começar. |

O catálogo informa as versões disponíveis. Em uma sessão na nuvem, o executor precisa aceitar a seleção de plugins do seu dispositivo. O Genius aplica essa seleção aos executores da sua conta que oferecem o recurso.

## Instalar os plugins

1. Abra o menu do Genius e entre em **Configurações → Plugins**.
2. Expanda **Disponíveis no catálogo**.
3. Localize **GitHub CLI (gh)** e selecione **Instalar**. Instale **Radicle (rad)** do mesmo modo se for usá-lo.
4. Aguarde cada plugin aparecer em **Instalados** com o estado **Ativo**.
5. Se você já tiver alterado permissões do plugin, expanda o item e confira **Ferramentas de desenvolvimento**. Para o GitHub CLI, a opção é **Usar a CLI do GitHub (gh)**. Para o Radicle, é **Usar o Radicle**.

O Genius verifica o catálogo e a integridade dos arquivos dos plugins. No ambiente que roda os comandos, o primeiro uso pode demorar mais porque o Genius prepara os binários conforme a necessidade. Aguarde o resultado antes de repetir a verificação.

### Conectar a conta GitHub

Para fazer consultas autenticadas, abra **Configurações → Catálogo → Integrações → GitHub** nas configurações do Genius e selecione **Conectar e instalar** ou **Conectar novamente**, conforme o estado exibido. Conclua a autorização no navegador e volte ao Genius. Use a conta que tem acesso aos repositórios que você pretende consultar.

O `gh` fornecido pelo plugin usa a autorização da integração. O Genius mantém a credencial no serviço, fora do ambiente dos comandos e scripts. Faça o login pela tela de integrações e mantenha senhas, tokens e códigos de autorização fora da conversa. A autorização do GitHub vale para o GitHub. A autorização do executor na nuvem usa sua conta Sufficit.

## Usar no Linux

1. Abra uma conversa cujo dispositivo seja **Este dispositivo**.
2. Peça que o Genius execute a [verificação dos comandos](#verificar-os-comandos) no shell dessa conversa.
3. Confira os caminhos e as versões. Se houver um `gh` instalado no sistema, o caminho do comando permite verificar se a conversa está usando o plugin do Genius.

Se o Genius pedir confirmação para usar o shell, confira os comandos exibidos antes de aprovar. A verificação abaixo usa comandos de leitura.

## Usar no Android

1. Instale e confirme o estado dos plugins no aplicativo.
2. No menu de criação de conversas, selecione **Conversa na nuvem**. Esse fluxo cria uma conversa nova em um executor exclusivo.
3. Aguarde a preparação do ambiente. Se o Genius abrir a página de autorização, conclua a etapa com sua conta Sufficit e volte ao aplicativo.
4. Na conversa, confira **Dispositivo da sessão**. Aguarde o ambiente **Nuvem** ficar acessível.
5. Envie a solicitação da [verificação dos comandos](#verificar-os-comandos). Os binários Linux rodam no executor. O Android envia as mensagens e apresenta os resultados.

### Conversas que já estão no celular

Para uma conversa iniciada no celular, confira a disponibilidade em
[Migrar uma conversa existente](dispositivos-e-nuvem.md#migrar-uma-conversa-existente).
Se a migração estiver indisponível, use **Conversa na nuvem** para o novo
trabalho. A conversa existente permanece no celular.

## Verificar os comandos

Em uma conversa de teste, você pode pedir ao Genius:

> Execute no shell desta sessão apenas os comandos abaixo e mostre a saída de cada um, inclusive os erros. Use somente o dispositivo desta conversa.

```sh
command -v gh
gh --version
command -v rad
rad --version
```

| Verificação | Como interpretar |
| --- | --- |
| `command -v gh` | Um caminho terminado em `/shims/github/gh` indica que o shell está usando o intermediário do Genius. Um caminho como `/usr/bin/gh` indica que o shell escolheu a instalação do sistema. Ela pode ter a mesma versão do catálogo. |
| `gh --version` | Exibe a versão do GitHub CLI. Use essa saída junto com o caminho para confirmar a origem do comando. |
| `command -v rad` | Um caminho que inclui `toolchain-radicle` indica que o shell selecionou o binário do plugin. Se a saída estiver vazia, o shell não encontrou `rad` no caminho de busca. |
| `rad --version` | Exibe a versão do Radicle em uso. |

Se você já conectou a conta GitHub, faça uma consulta autenticada de leitura. Este comando retorna apenas o tipo da conta, como `User`.

```sh
gh api --method GET /user --jq .type
```

Para outras consultas REST, indique o método `GET` explicitamente ao passar parâmetros para `gh api`. No `gh` intermediado pelo Genius, comandos de gerenciamento de credenciais, como `gh auth`, ficam reservados à tela de integrações.

## Revogar, desativar ou remover

Abra **Configurações → Plugins → Instalados** e localize o plugin.

- Para retirar apenas a capacidade, expanda o item e desligue **Usar a CLI do GitHub (gh)** ou **Usar o Radicle**, conforme o plugin.
- Para desativar o plugin, desligue a chave **Ativo**.
- Para desinstalar o plugin, selecione **Remover**.

Em um executor próprio compatível, a mudança se aplica à seleção usada para os comandos seguintes quando o Genius sincroniza a configuração. A mudança não encerra um comando que já foi iniciado. Se você precisar parar esse comando, use o controle de cancelamento da própria execução. Após a retirada do plugin, um binário já instalado no sistema pode continuar disponível. Repita `command -v` para conferir qual caminho ficou ativo.

## Resolver problemas

| Sintoma | O que conferir |
| --- | --- |
| O plugin não aparece no catálogo. | Confirme que a fonte oficial do catálogo está disponível. Se a tela indicar falha ao consultar o catálogo, aguarde a conexão voltar e abra **Plugins** novamente. |
| No Android, a conversa mostra um dispositivo local. | Abra **Conversa na nuvem**, autorize o ambiente se solicitado e confirme a indicação **Nuvem** na conversa. |
| O ambiente ainda está preparando ou pede autorização. | Aguarde a preparação. Se houver uma página de autorização aberta, conclua-a com sua conta Sufficit e volte para a mesma conversa. |
| A conversa na nuvem usa `/usr/bin/gh` ou `rad` não aparece. | Confira se o executor é da sua conta e se os plugins aparecem como **Ativo** com as permissões ligadas. Se estiver tudo certo, volte à lista de conversas, abra novamente a mesma conversa na nuvem e repita os comandos. Em versões com falha de seleção na primeira conexão, a reabertura pode aplicar a configuração. |
| O `gh` do Genius pede para conectar a conta GitHub. | Conclua a autorização em **Configurações → Catálogo → Integrações → GitHub**. Depois repita a consulta autenticada. Se a conta estiver conectada e um repositório continuar inacessível, confira se essa conta tem permissão para ler o repositório. |
| O comando continua disponível após remover o plugin. | Confira o caminho com `command -v`. O ambiente pode ter outra instalação da mesma ferramenta. |

Se o problema continuar, informe ao suporte a versão do Genius, o tipo de dispositivo da sessão, o estado dos plugins e a saída dos comandos de verificação. Remova nomes de repositórios privados, dados de conta e credenciais antes de compartilhar.

[Voltar ao guia do Genius](index.md) · [Manual oficial do GitHub CLI](https://cli.github.com/manual/gh_api) · [Documentação do Radicle](https://radicle.dev/guides/user)

Última revisão em 26/11/2026. Área responsável pelo conteúdo: Sufficit AI.
