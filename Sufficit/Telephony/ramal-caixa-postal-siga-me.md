# Ramal, caixa postal e siga-me

Namespace: `Sufficit.Telephony`

## Objetivo

Explicar o que pertence ao ramal e o que é uma aplicação separada no plano de
discagem. Em outros sistemas de telefonia, o próprio ramal costuma ter correio de
voz e desvio de chamadas. Na Sufficit, não.

## O que é do ramal

- Os aparelhos registrados (extensão do Chrome, aplicativo, telefone de mesa).
- A presença e o "Não perturbe" (veja [Presença do ramal](presenca-ramal.md)).
- A preferência de gravação das chamadas.

## O que não é do ramal

| Recurso | Na Sufficit |
| --- | --- |
| Correio de voz | Não existe correio de voz por ramal. A **caixa postal** é uma aplicação separada, com cadastro próprio, que recebe recados quando um fluxo de atendimento encaminha a ligação para ela (veja [Caixas postais](caixas-postais.md)). |
| Desvio de chamadas (siga-me) | O ramal não tem desvio. O **siga-me** é uma aplicação separada, usada como destino no plano de discagem (por exemplo, no fluxo de atendimento fora do expediente), e liga para o número configurado nele. |

## Consequências

- Ligação direta para um ramal que não atende, está sem aparelho conectado ou
  está com todos os aparelhos em "Não perturbe" **termina** como indisponível ou
  sem resposta. Ela não vai para uma caixa postal nem para outro número por conta
  do ramal.
- Para recados ou para seguir para outro número, o fluxo de atendimento (plano de
  discagem) precisa ter a caixa postal ou o siga-me como destino.
- Clientes que vieram de outros sistemas costumam procurar "correio de voz do
  ramal" ou "desvio do ramal". A orientação é configurar o fluxo de atendimento.

## Exemplo fictício

A "Clínica Exemplo" quer receber recados quando a recepção não atende. Em vez de
procurar um correio de voz no ramal 6001, o fluxo de atendimento da linha
principal toca o ramal e, sem resposta, segue para a caixa postal "Recados da
recepção". Fora do expediente, o mesmo fluxo usa o siga-me para o celular da
gerente.

## Fluxos relacionados

- [Caixas postais](caixas-postais.md)
- [Presença do ramal e "Não perturbe"](presenca-ramal.md)
- [Voltar ao índice de Telefonia](index.md)

Última revisão: 24/11/2026. Área responsável: Telefonia.
