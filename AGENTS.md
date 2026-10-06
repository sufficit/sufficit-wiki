# Instruções para agentes — Wiki pública Sufficit

## Propósito e público

Este repositório é a base pública de conhecimento do CRM/ERP Sufficit, um produto em desenvolvimento que será comercializado no futuro. Documenta fluxos de negócio, funcionalidades, conceitos e comportamento do produto para clientes, potenciais clientes, parceiros, integradores e equipes de suporte.

A documentação deve ser pública por intenção. Escreva para alguém que não conhece a operação interna da Sufficit e precisa entender como usar o produto e quais regras se aplicam. Informações sobre o funcionamento podem ser publicadas quando não contiverem dados sensíveis.

## Escopo

Documentar:

- Fluxos de contratação, serviços, renovação, cobrança, pagamentos, créditos e cancelamento.
- Estados, transições, permissões funcionais, pré-requisitos e regras de negócio.
- Passos no produto, resultados esperados, limites, exceções e recuperação de falhas.
- Integrações e interfaces destinadas ao público, com exemplos fictícios.
- Diferenças entre funcionalidades disponíveis, legadas, em validação e planejadas.
- Conceitos e perguntas frequentes necessários para compreender o CRM/ERP.

Procedimentos internos de infraestrutura, incidentes privados, acesso a produção e instruções administrativas restritas pertencem aos repositórios internos apropriados. Quando um fluxo depender de configuração interna, explique o efeito e a condição para o usuário, sem publicar o mecanismo privado de acesso.

## Conteúdo público e dados sensíveis

Trate todo arquivo, imagem, anexo, diff e histórico deste repositório como acessível ao público.

Nunca incluir:

- Senhas, tokens, chaves, cookies, credenciais, strings de conexão ou URLs com segredos.
- Dados reais de clientes ou usuários: nomes identificáveis, documentos, contatos, endereços, identificadores de contas, contratos, pagamentos ou transações.
- Extratos, faturas, valores negociados, logs ou capturas de tela que exponham informações reais ou confidenciais.
- Topologia interna, endereços privados, hosts operacionais, portas administrativas, caminhos de acesso ou instruções que facilitem acesso indevido.
- Links para tickets, conversas, documentos ou sistemas privados como fonte necessária à compreensão de uma página pública.
- Condições comerciais internas, custos de fornecedores ou informações protegidas por contrato.

Use dados inteiramente fictícios e identifique exemplos como ilustrativos. Substituir apenas o nome de um cliente não basta: todos os campos e metadados devem ser revisados. Confira também URLs, nomes de arquivos, propriedades de imagens e conteúdo de anexos.

Não copie documentos internos integralmente. Extraia a regra pública, reescreva para o público do produto e revise antes de adicionar. Descrever uma funcionalidade não autoriza divulgar os dados usados para verificá-la.

Se encontrar um segredo, não o reproduza no chat, nos commits ou em relatórios. Interrompa sua publicação e informe o responsável. Remover do arquivo atual não remove o histórico; revogação e tratamento do histórico precisam ser coordenados com o responsável.

## Evidência e fidelidade ao produto

Antes de afirmar uma regra, consulte a implementação, documentação oficial ou decisão explícita do responsável pelo produto. Diferencie fatos verificados de hipóteses; não invente regras para preencher lacunas.

- Código implementado não prova que a funcionalidade está disponível no ambiente do cliente.
- Uma funcionalidade planejada não deve ser apresentada como disponível nem como promessa comercial.
- Uma configuração padrão não prova que todos os ambientes usam esse valor.
- Comportamento exclusivo da operação interna Sufficit não deve ser apresentado como regra universal do CRM/ERP.
- Não confunda renovação, geração de competência, emissão de cobrança, pagamento confirmado e liberação operacional. Explique separadamente quando esses eventos ocorrerem em etapas distintas.
- Distinga estado do tipo no catálogo, estado do contrato e estado financeiro quando forem entidades diferentes.

Declare condições de disponibilidade, configuração e versão quando relevantes. Se não houver comprovação, registre a limitação e peça esclarecimento ao responsável antes de apresentar o comportamento como definitivo.

Fontes publicadas devem ser acessíveis ao público. Prefira links permanentes para código público quando a referência técnica ajudar. Não use caminhos absolutos de máquinas do workspace nem exponha referências privadas; mantenha a evidência interna no local apropriado.

## Forma das páginas

Escreva em português do Brasil, com linguagem simples, direta e consistente. Explique siglas na primeira ocorrência e use os nomes exibidos no produto. Evite linguagem promocional, jargão desnecessário e afirmações absolutas sem evidência.

Cada página de fluxo deve conter, proporcionalmente ao assunto:

1. Objetivo: o que o usuário consegue fazer.
2. Disponibilidade: disponível, legado, em validação ou planejado; versão quando conhecida.
3. Pré-requisitos: perfil/permissão funcional, configuração e estado necessário.
4. Passos: ações do usuário em ordem e resultado esperado.
5. Regras: datas, estados, valores e efeitos relevantes.
6. Exceções: bloqueios, mensagens, tentativa novamente e como obter ajuda.
7. Exemplo fictício quando ajudar a compreensão.
8. Fluxos relacionados e fontes públicas, quando houver.
9. Data da última revisão e área responsável, sem contatos pessoais privados.

Não declare uma página revisada apenas por ter sido editada: revisão exige conferir as regras descritas. Diagramas Mermaid e tabelas são úteis quando esclarecem decisões, estados ou sequências.

## Organização e manutenção

- Use Markdown como fonte principal e links relativos entre páginas.
- Organize por domínio e tarefa do usuário, evitando reproduzir a estrutura dos projetos de código.
- Mantenha um índice navegável; inclua páginas novas no índice existente.
- Prefira nomes estáveis em minúsculas, com hífens e sem espaços para páginas públicas.
- Preserve links ao mover páginas; atualize as referências afetadas.
- Mantenha uma página canônica para cada regra; outras páginas devem referenciá-la em vez de duplicá-la.
- Detalhes técnicos específicos podem continuar no projeto de origem; a wiki centraliza a explicação pública do fluxo.
- Atualize as páginas relacionadas quando uma mudança alterar comportamento, termos ou estados.
- Não migre toda a documentação nem desenvolva um portal sem uma solicitação que autorize esse escopo.

Planos de execução, quando solicitados ou necessários, ficam em `docs/PLAN-*.md`, nunca na raiz. Registros de atividade seguem a convenção local em `docs/activities/`. Esses arquivos também são públicos e devem obedecer às mesmas restrições; não transforme a wiki em arquivo de tarefas internas. Confira as convenções existentes antes de criar novos documentos.

## Validação e entrega

Antes de concluir uma mudança:

- Confira precisão das regras e indicação de disponibilidade.
- Revise arquivos e diff para dados sensíveis e referências internas.
- Valide links relativos, imagens, âncoras e inclusão no índice.
- Execute os validadores e o build de documentação existentes, quando aplicáveis; não crie infraestrutura de testes apenas para uma edição simples.
- Preserve alterações de outras pessoas e informe o que foi validado e o que continua incerto.

Este repositório é público: workflows GitHub Actions devem usar runners hospedados pelo GitHub, como `ubuntu-latest`. A frota privada self-hosted Sufficit não deve ser usada aqui.

Criar ou editar documentação não autoriza alterar produção, banco, credenciais, configuração de clientes ou executar os fluxos descritos. Publicação, push, merge e implantação seguem a autorização do usuário para a tarefa; não presuma autorização apenas porque o conteúdo é público.
