# Filas: ramal ocupado, sem resposta e sem aparelho

Namespace: `Sufficit.Telephony`

## Objetivo

Explicar o que a fila faz quando oferece uma chamada a um atendente e ela não é
atendida: ramal ocupado, sem resposta ou sem nenhum aparelho disponível. Também
mostra onde ajustar cada tempo no cadastro da fila.

## Disponibilidade

| Recurso | Situação |
| --- | --- |
| "Espera após ramal ocupado (segundos)" nas opções de distribuição da fila | Disponível desde 23/11/2026. Até a correção de 24/11/2026 o tempo não era aplicado e o ramal ocupado voltava a receber oferta a cada poucos segundos. |
| Fila sem tocar aparelho em "Não perturbe" ou Offline (presença) | Disponível desde 24/11/2026. Veja [Presença do ramal](presenca-ramal.md). |

## O que acontece em cada caso

| Resultado da oferta | O que a fila faz | Onde ajustar |
| --- | --- | --- |
| Ramal ocupado (recusou a chamada, por exemplo com "Não perturbe" no próprio telefone ou aplicativo) | Deixa o ramal fora das ofertas de **todas** as filas e servidores pela "Espera após ramal ocupado". Depois volta a oferecer normalmente. | "Espera após ramal ocupado (segundos)": padrão 10, de 0 a 300 |
| Sem resposta (tocou e ninguém atendeu) | Oferece de novo depois do "Intervalo entre tentativas". | "Toque por atendente (segundos)" e "Intervalo entre tentativas (segundos)" |
| Nenhum aparelho disponível (ramal não registrado, ou todos os aparelhos em "Não perturbe" ou Offline) | Não chama o ramal: nenhum aparelho toca e nada é gravado. Tenta de novo depois do "Intervalo entre tentativas". | "Intervalo entre tentativas (segundos)" |
| Atendida em outro ramal | Para de tocar nos demais. | — |

## Regras da "Espera após ramal ocupado"

- Não é pausa: nada fica registrado no atendente. Terminado o tempo, ele volta a
  receber ofertas sozinho.
- Vale para todas as filas de que o ramal participa e em todos os servidores de
  voz, não só na fila que ofereceu.
- Se o "Intervalo entre tentativas" for maior, vale o maior dos dois.
- Com 0, a fila segue apenas o "Intervalo entre tentativas" (comportamento antigo).
- Ocupado também conta para a autopausa quando "Contar ocupado para autopausa"
  está ligado.

## Por que isso importa

Um ramal com "Não perturbe" ligado no próprio telefone (MicroSIP, por exemplo)
recusa cada oferta na hora. Sem a espera, a fila voltava a oferecer a cada um ou
dois segundos: em 24/11/2026 isso gerou dezenas de milhares de tentativas e de
gravações vazias num único servidor. No painel de telefonia esses ramais aparecem
com a tag **DND?** ("Não perturbe provável").

Para que a fila nem ofereça a chamada, o atendente deve usar a disponibilidade dos
aplicativos Sufficit (extensão do Chrome ou Sufficit Phone) em vez do "Não
perturbe" do próprio telefone. Veja [Presença do ramal](presenca-ramal.md).

## Exemplo fictício

A fila "Atendimento" da "Clínica Exemplo" usa toque de 20 segundos, intervalo
entre tentativas de 2 segundos e espera após ramal ocupado de 10 segundos. O ramal
6005 está com "Não perturbe" ligado no MicroSIP. A fila oferece a chamada, o 6005
recusa como ocupado e fica 10 segundos fora de todas as filas, enquanto os outros
atendentes continuam recebendo. Depois disso a fila tenta o 6005 de novo.

## Fluxos relacionados

- [Presença do ramal e "Não perturbe"](presenca-ramal.md)
- [Ramal, caixa postal e siga-me](ramal-caixa-postal-siga-me.md)
- [Gravação de chamadas](gravacao-chamadas.md)
- [Voltar ao índice de Telefonia](index.md)

Última revisão: 24/11/2026. Área responsável: Telefonia.
