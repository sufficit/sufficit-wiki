---
title: Ferramentas, integrações e permissões no Genius
permalink: /ai/genius/ferramentas-e-permissoes/
redirect_from:
  - /Genius/ferramentas-e-permissoes/
---

# Ferramentas, integrações e permissões

Namespace `Sufficit.AI.Genius`.

O agente consulta o catálogo para descobrir os recursos disponíveis para uma tarefa. A disponibilidade pode mudar conforme o dispositivo da sessão, o que estiver instalado e a autorização da sua conta. Confira o dispositivo antes de conectar uma integração ou autorizar uma operação.

## Entender os recursos

| Recurso | Para que serve |
| --- | --- |
| **Ferramenta** | Permite executar uma operação, como ler um arquivo autorizado ou consultar um serviço conectado. |
| **Habilidade** | Orienta o agente a seguir um procedimento. As instruções usam as ferramentas que a sessão oferece. |
| **Integração** | Conecta o Genius à conta de um serviço externo mediante autorização. |
| **Plugin** | Adiciona uma capacidade instalada pelo Genius, como o GitHub CLI ou o Radicle. |
| **Servidor MCP** | Oferece ferramentas e referências a um cliente pelo Protocolo de Contexto de Modelo. A disponibilidade depende da conexão e das permissões. |

## Descobrir e configurar

1. No Genius, abra **Configurações → Catálogo**.
2. Use **Buscar recursos** ou o filtro correspondente, como **Integrações** ou **Habilidades**.
3. Abra o recurso para conferir as opções de instalação, conexão ou configuração. Se o Genius pedir login, conclua a autorização no navegador.
4. Volte à conversa e peça uma verificação de leitura apropriada ao serviço. Por exemplo, consulte a configuração de um projeto fictício ao qual a conta conectada tenha acesso.

Se você estiver procurando um plugin, use **Configurações → Plugins** e confira **Disponíveis no catálogo**. Os passos para ferramentas Linux estão no [manual de GitHub CLI e Radicle](toolchain.md).

Configurar um recurso no dispositivo selecionado aplica a alteração àquele ambiente, conforme o tipo de recurso. Confira o dispositivo antes de repetir a configuração em outra instalação.

## Revisar pedidos de confirmação

Quando a política da sessão pedir confirmação, o Genius mostra a ação na conversa. Leia a ferramenta, o destino e os dados que ela pretende usar. Aprove quando a ação corresponder ao pedido. Se o destino ou a conta estiverem incorretos, recuse e informe o que deve ser corrigido.

Conectar uma conta libera o uso da integração dentro das permissões dessa conta e da sessão. Uma autorização de login e a confirmação de uma ação específica são etapas diferentes. Se você precisar retirar uma capacidade de plugin, use as permissões do plugin. Se quiser encerrar a conexão da conta, confira na integração o alcance de **Encerrar conta** antes de confirmar.

## Usar o navegador

Em um desktop compatível, o Genius pode usar uma extensão de navegador para trabalhar em uma aba da conversa no perfil conectado. O recurso depende da extensão, do dispositivo e de um perfil disponível. Um executor na nuvem pode ter um navegador próprio, com sessão de login separada.

- Confira o dispositivo, o perfil e a conta exibida antes de aprovar alterações em um site.
- Se a página exigir login ou uma verificação do titular, conclua essa etapa no navegador oficial.
- Se uma operação não refletir o resultado esperado, confira o estado atual da página antes de repeti-la. Por exemplo, verifique se o item já aparece na lista depois de clicar em **Salvar**.

## Quando um recurso não aparece

Confirme se você está na conversa e no dispositivo esperados. Depois confira se a ferramenta está instalada, se a integração tem conexão e se sua conta tem permissão para a tarefa. Para ajudar o suporte, informe o nome do recurso, o dispositivo da sessão e a mensagem exibida, sem compartilhar senhas ou tokens.

[Guia do Genius](index.md) · [Dispositivos e nuvem](dispositivos-e-nuvem.md) · [Privacidade e suporte](privacidade-e-suporte.md)

Última revisão em 26/11/2026. Área responsável pelo conteúdo: Sufficit AI.
