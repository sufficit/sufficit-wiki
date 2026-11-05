# Limites dos planos de saída de chamadas

Namespace: `Sufficit.Telephony`

Compare a quantidade de ligações admitidas e o número de ligações simultâneas de cada plano. A empresa precisa ter o serviço contratado e habilitado; a disponibilidade de cada modalidade depende do catálogo utilizado na contratação.

## Planos e limites

| Plano | Canais simultâneos | Limite de tentativas de saída | Regra e disponibilidade |
| --- | ---: | --- | --- |
| Individual (SINGLE) | 1 | 90 nas últimas 72 horas | Disponível; equivale à referência de 30 por dia, com flexibilidade entre os dias. |
| Flexível (FLEX) | 4 | 210 nas últimas 72 horas | Modalidade do catálogo novo; referência de 70 por dia. É distinta do Flexível+. |
| Flexível+ (FLEX+) | 4 | 450 nas últimas 72 horas | Preserva o patamar do antigo Compartilhado; referência de 150 por dia. |
| Fixo ilimitado | 1 por assinatura/canal contratado | Sem teto de quantidade de tentativas | Referência de alerta prevista: 50 chamadas/dia. Não é franquia de bloqueio; a disponibilidade do alerta depende da versão. |
| Móvel ilimitado | 1 por assinatura/canal contratado | Sem teto de quantidade de tentativas | Referência de alerta prevista: 50 chamadas/dia. Não é franquia de bloqueio; a disponibilidade do alerta depende da versão. |
| Tarifado (BILLED) | Conforme contratação; padrão operacional de 10 | Sem franquia fixa de quantidade de tentativas | Consumo cobrado por tempo, conforme tarifa e condições de crédito aplicáveis. |
| Livre (FREE) | 1 | Referência prevista de 10 nas últimas 24 horas | A aplicação desse limite não está confirmada em todas as versões; não usar como garantia de disponibilidade ou bloqueio. |

Individual, Flexível e Flexível+ não têm franquia de minutos de fala nesta regra; o controle descrito é de tentativas e canais. Destinos habilitados, crédito e demais condições do contrato continuam aplicáveis. Nos ilimitados, os destinos dependem da modalidade contratada: fixos ou móveis e eventuais destinos adicionais habilitados.

## Compartilhado corresponde ao Flexível+

O **Flexível+ é o equivalente do antigo Compartilhado**: quatro canais e o patamar de 450 tentativas em 72 horas. O Flexível de 210 tentativas é menos permissivo e não deve substituir automaticamente esses contratos.

A atualização do nome não autoriza reajuste, redução de franquia nem alteração do preço negociado. Quando houver mudança de referência de preço no catálogo, preserve o valor contratado mediante a condição comercial ou desconto correspondente. Uma troca deliberada para outro plano exige uma alteração contratual própria.

Um cadastro antigo chamado apenas “Flexível” pode representar as condições históricas. Para conferir a equivalência, verifique a modalidade e seus limites efetivamente contratados, além do nome. Uma mudança específica já acordada para outro plano deve ser respeitada.

## Como funciona a janela de 72 horas

A janela é móvel: a cada nova tentativa, considera-se o uso das últimas 72 horas. Não há uma renovação de toda a franquia à meia-noite ou a cada três dias do calendário.

**Exemplo fictício:** uma empresa com Flexível+ realizou 300 tentativas que ainda estão dentro da janela. Restam 150, desde que não existam outras tentativas nesse período. A capacidade volta a ficar disponível à medida que as tentativas anteriores completam 72 horas.

Conta a tentativa admitida e encaminhada pelo tronco, inclusive quando o destino não atende. Ligações rejeitadas antes de sair pelo tronco não entram nessa contagem. O número de canais limita quantas saídas podem ocorrer ao mesmo tempo, independentemente de ainda existir franquia na janela.

## Ao atingir um limite

Novas saídas podem ser recusadas por falta de canal disponível ou por atingir o limite da janela. Outro serviço de saída contratado pode ser utilizado quando houver uma rota habilitada para ele; isso não é automático em toda contratação.

Para conferir uma divergência, consulte o plano, os canais e a janela de utilização. Informe ao suporte o horário da tentativa e o serviço contratado. Um relatório de chamadas atendidas, isoladamente, não reproduz a contagem de tentativas admitidas.

## Páginas relacionadas

- [Tronco individual](tronco-individual.md)
- [Telefonia](index.md)
- [Wiki Sufficit](../../README.md)

Última revisão: 05/11/2026. Área responsável: Telefonia.
