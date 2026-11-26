---
title: Dispositivos e conversas na nuvem no Genius
permalink: /Genius/dispositivos-e-nuvem/
---

# Dispositivos e conversas na nuvem

Namespace `Sufficit.AI.Genius`.

O **Dispositivo da sessão** indica onde o agente executa as ferramentas. Você pode ler uma conversa pelo celular enquanto o agente trabalha em outro computador. A disponibilidade de arquivos, navegador e comandos segue o dispositivo que executa a sessão e as permissões que ele oferece.

## Escolher o ambiente

| O que você precisa | Qual ambiente escolher |
| --- | --- |
| Trabalhar com arquivos e aplicativos do computador em que está usando o Genius. | **Este dispositivo**, com as permissões necessárias. |
| Retomar uma conversa que já está em outro dispositivo da sua conta. | Abra a conversa existente na lista e aguarde a conexão com o dispositivo de origem. |
| Começar um trabalho novo em um ambiente remoto. | **Conversa na nuvem**, quando o recurso estiver disponível na conta e na versão. |
| Levar uma conversa existente e os arquivos vinculados para a nuvem. | **Migrar para a nuvem**, a partir de um dispositivo de origem com suporte à migração. |

Um **espaço de trabalho** é a pasta vinculada ao trabalho da conversa. Ao preparar um pedido que usa arquivos, confira se eles estão anexados ou acessíveis no espaço de trabalho do dispositivo da sessão.

## Criar uma conversa na nuvem

1. No menu de criação, selecione **Conversa na nuvem**.
2. Aguarde enquanto o Genius prepara um computador remoto, chamado de executor.
3. Se aparecer uma página para autorizar a conta Sufficit, conclua a autorização no navegador e volte ao Genius.
4. Confira se a conversa indica **Nuvem** e aguarde o ambiente ficar acessível antes de enviar a primeira solicitação.
5. Envie os arquivos necessários como anexos ou vincule um espaço de trabalho disponível no ambiente.

A criação começa em uma conversa nova, com espaço de trabalho próprio. Arquivos e mensagens de outras conversas continuam na origem. Para usar `gh` ou `rad` nesse ambiente, veja [GitHub CLI e Radicle](toolchain.md).

## Migrar uma conversa existente

Em um dispositivo de origem e uma versão compatíveis, abra o menu da conversa e selecione **Migrar para a nuvem**. Confira a conversa selecionada e os arquivos do espaço de trabalho antes de iniciar.

1. Aguarde a preparação e autorize a conta Sufficit se o aplicativo solicitar.
2. Deixe o Genius aguardar a conclusão das mensagens e execuções pendentes da conversa de origem.
3. Quando o aplicativo abrir a conversa no destino, confira **Dispositivo da sessão**, histórico e arquivos antes de continuar.

Quando a conversa divide o espaço de trabalho com outras sessões, o Genius pode criar um espaço exclusivo com uma cópia dos arquivos para a conversa migrada. As outras sessões e suas pastas de origem ficam disponíveis. Alterações posteriores nessas duas cópias seguem separadamente. Arquivos de outras pastas precisam estar no espaço de trabalho para entrar na transferência.

Nas versões Android verificadas até 26/11/2026, incluindo a versão `0.184.0`, uma conversa iniciada localmente no celular ainda não podia ser migrada por esse fluxo. O comando pode aparecer e ser recusado. Nesse caso, crie uma **Conversa na nuvem** e envie apenas o contexto que você pode compartilhar com o novo ambiente.

## Se o dispositivo estiver indisponível

- Se a conversa indicar um dispositivo offline, confirme que o Genius está aberto no dispositivo remoto e que ele tem conexão para receber o acesso.
- Se você estiver usando um executor, aguarde o estado de preparação ou reconexão. Conclua a autorização no navegador quando ela for solicitada.
- Se a migração oferecer **Tentar novamente**, use a opção para consultar o estado da transferência e retomar o fluxo. Confira se a conversa já aparece no destino antes de repetir uma ação.
- Se a mensagem ainda estiver aguardando confirmação de entrega, confira o estado da conversa e da fila antes de enviar outra cópia.

[Guia do Genius](index.md) · [Conversas e arquivos](conversas.md) · [Ferramentas e permissões](ferramentas-e-permissoes.md)

Última revisão em 26/11/2026. Área responsável pelo conteúdo: Sufficit AI.
