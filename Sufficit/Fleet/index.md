---
title: Guia do Sufficit Fleet
permalink: /ai/fleet/
---

# Guia do Sufficit Fleet

Namespace `Sufficit.Fleet`.

O Fleet organiza o trabalho de agentes. Você pode configurar agentes, acompanhar suas tarefas e definir quando eles participam de uma conversa. A disponibilidade dos canais depende da configuração da sua empresa e das permissões da sua conta.

## Modos de resposta em grupos do WhatsApp

Use os modos abaixo em um grupo integrado ao Fleet com um agente anfitrião. O modo define quando o agente pode responder no grupo. O acesso às ferramentas e a autorização para executar ações seguem as permissões da integração.

| Modo | Quando o agente responde | Quando usar |
| --- | --- | --- |
| **Suporte** (`support`) | O Fleet trata as mensagens dos participantes como dirigidas ao agente. Ele pode responder inclusive quando uma mensagem menciona outra pessoa. | Quando o grupo funciona como um canal de atendimento do agente. |
| **Menção** (`mention`) | O agente responde quando o Fleet reconhece seu nome, a referência `@agente` ou uma resposta a uma mensagem dele. As demais mensagens ficam no histórico, sem iniciar uma resposta. | Quando as pessoas conversam entre si e chamam o agente apenas quando precisam dele. |
| **Discreto** (`discreet`) | O agente responde quando é chamado por `@agente` ou por uma resposta a uma mensagem dele. Em outros casos, pode intervir se identificar uma contribuição relevante para o objetivo do grupo e justificar a intervenção. | Quando o grupo quer ajuda pontual sem precisar chamar o agente em todas as ocasiões. |

Grupos criados ou adotados com um agente anfitrião começam em **Suporte**. Se o dono do grupo já escolheu outro modo, essa escolha vale para o grupo.

## Alterar o modo de resposta

1. Como dono do grupo, abra sua conversa privada autorizada com o Fleet no WhatsApp.
2. Informe o nome do grupo e o modo. Em um grupo fictício, você poderia pedir “Mude o grupo Equipe de Testes para o modo Menção”.
3. Confira se o Fleet confirmou o grupo e o modo. Se houver grupos com nomes parecidos, identifique o grupo correto antes de confirmar.
4. Para testar **Menção**, envie uma mensagem entre participantes e depois dirija uma pergunta ao agente com `@agente`. Somente a pergunta dirigida ao agente deve iniciar uma resposta.

Em **Menção**, escrever o nome do agente pode acionar uma resposta. Use `@agente` ou responda a uma mensagem dele quando quiser deixar claro o destinatário.

## Guias relacionados

- [Sufficit AI](../AI/index.md)
- [Guia do Genius](../AI/Genius/index.md)

Revisado em 27/11/2026 pela equipe do Sufficit Fleet.
