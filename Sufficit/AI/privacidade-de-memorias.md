---
permalink: /AI/privacidade-de-memorias/
---

# Privacidade de memórias

Namespace `Sufficit.AI`.

No Genius, você pode pedir para lembrar uma preferência ou decisão. O Sufficit AI guarda a memória e usa sua conta autenticada para identificar o titular.

| Você quer | Como pedir ao Genius | Visibilidade |
| --- | --- | --- |
| Guardar uma memória pessoal | Peça para lembrar a informação. | Privada por padrão. |
| Organizar uma memória pessoal em um contexto | Indique o contexto ao pedir para lembrar. Você pode usar contextos diferentes para separar assuntos. | Privada por padrão, mesmo dentro do contexto de uma empresa. |
| Compartilhar com a empresa | Peça explicitamente para compartilhar e indique a empresa. Você precisa ter acesso ao contexto dela. | Disponível a quem tem acesso ao contexto daquela empresa. |

Por exemplo, você pode pedir **“Guarde como memória privada, no contexto da Empresa Exemplo, que eu prefiro revisar os relatórios de manhã”**. A preferência entra no seu acervo pessoal associada à Empresa Exemplo. Para disponibilizar uma regra de trabalho à empresa, peça **“Compartilhe com a Empresa Exemplo a regra de revisar os relatórios às segundas-feiras”**.

Em integrações, `contextId` identifica o contexto. `privacyLevel` controla a visibilidade. Ao criar uma memória, omitir `privacyLevel` ou enviar `private` mantém a memória privada. Enviar `tenant` explicitamente com o contexto da empresa solicita o compartilhamento. Se o Genius não conseguir identificar um contexto autorizado, informe qual contexto você quer usar.

O padrão privado vale para novas gravações nas integrações atualizadas do Sufficit AI. As memórias já gravadas conservam a visibilidade registrada.

[Voltar ao índice Sufficit AI](index.md).

Revisão em 21/11/2026. Área responsável: Sufficit AI.
