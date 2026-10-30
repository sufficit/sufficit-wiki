# Tronco individual

Namespace: `Sufficit.Telephony`

O tronco individual é o serviço de saída mais simples da telefonia Sufficit. Ele permite que a empresa faça ligações para números externos por um canal, com identificação de chamada e um limite de ligações por período.

## Disponibilidade e pré-requisitos

Disponível na telefonia Sufficit para empresas que contrataram o tronco individual. A empresa pode ter apenas um tronco individual ativo.

O tronco individual não pode ser combinado com os troncos flexíveis (Flex ou Flex+). A empresa precisa escolher entre eles.

## Regras

| Regra | Valor |
| --- | --- |
| Canais | 1 ligação externa por vez |
| Duração das ligações | Sem limite de minutos |
| Ligações externas | 30 por dia, contadas como 90 a cada 3 dias (72 horas) |
| Destinos | Qualquer número válido |
| Identificação de chamada | Sempre ativa: o destino vê o número da empresa |

### Por que a conta é feita em 3 dias

O limite é de 30 chamadas por dia, mas a contagem soma as últimas 72 horas. Assim a empresa tem flexibilidade: pode fazer mais de 30 ligações num dia movimentado, desde que o total dos últimos 3 dias não passe de 90.

Conta toda ligação que sai pelo tronco individual, mesmo que o destino não atenda. Ligações bloqueadas antes de sair, por exemplo por falta de canal livre, não entram na conta.

## Exceções

- Ao atingir o limite, novas ligações externas não saem pelo tronco individual até que chamadas antigas deixem a janela de 72 horas. Se a empresa tiver outro serviço de saída contratado, a ligação pode seguir por ele.
- Uma segunda ligação externa simultânea não sai pelo tronco individual, porque ele tem um único canal.
- Falhas temporárias nos sistemas internos de cobrança ou contagem não bloqueiam ligações autorizadas pelo serviço contratado.
- A contagem em janela de 3 dias está em implantação. Enquanto isso, alguns ambientes ainda contam 30 chamadas nas últimas 24 horas.

## Exemplo ilustrativo

Uma empresa fictícia faz 20 ligações na segunda-feira e 20 na terça. Na quarta, tem um dia de muitas ligações e consegue fazer até 50, porque o total dos 3 dias chega a 90. Na quinta, as ligações de segunda já saíram da janela e voltam a ficar disponíveis.

## Páginas relacionadas

- [Telefonia](index.md)
- [Wiki Sufficit](../../README.md)

Última revisão: 30/10/2026. Área responsável: Telefonia.
