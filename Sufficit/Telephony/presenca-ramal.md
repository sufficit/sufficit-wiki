# Presença do ramal e "Não perturbe"

Namespace: `Sufficit.Telephony`

## Objetivo

Mostrar a disponibilidade declarada de cada ramal no painel de telefonia e nas
filas: disponível, ausente, ocupado, "Não perturbe" ou indisponível. Esta página
também explica a diferença entre o "Não perturbe" **confirmado** e o
**provável**.

## Disponibilidade

| Recurso | Situação |
| --- | --- |
| Presença do ramal gravada no servidor de voz (API de presença) | Disponível desde 23/11/2026. |
| Painel de telefonia mostrando presença, "DND" e "DND?" | Disponível desde 23/11/2026. |
| Filas deixando de oferecer chamadas a ramais em "Não perturbe" ou indisponíveis | Disponível desde 23/11/2026. |
| Aplicativo Sufficit Phone alterando a presença pela disponibilidade escolhida | Planejado. |
| Extensão Sufficit Phone para Chrome alterando a presença pela disponibilidade escolhida (Disponível, Não perturbe, Offline = indisponível) | Disponível desde 24/11/2026 (versão 2.23.0). |
| Colegas vendo a presença pela tecla de monitoramento (BLF) do telefone | Planejado. |
| Opção no cadastro do ramal: presença unificada (vale para todos os aparelhos) ou por aparelho (extensão do Chrome, aplicativo e telefone de mesa separados) | Planejado. |

## Estados de presença

A presença é guardada no servidor de voz, identificada pelo código único do ramal
(não pelo número). O mesmo estado vale em todos os servidores de voz.

| Estado | O que significa | Filas | Painel |
| --- | --- | --- | --- |
| Sem estado | Nada foi declarado | Recebe chamadas | Estado normal do ramal |
| Disponível | Disponível | Recebe chamadas | Estado normal do ramal |
| Disponível para conversar | Disponível | Recebe chamadas | Estado normal do ramal |
| Ausente | Afastado por pouco tempo (ex.: almoço) | Recebe chamadas | "Ausente · nota" |
| Ocupado | Ausente com o motivo "ocupado" | Recebe chamadas | "Ocupado · nota" |
| Ausência prolongada | Férias, licença | Recebe chamadas | "Ausência prolongada · nota" |
| Não perturbe | Não quer receber chamadas | **Não recebe chamadas de fila** | Tag **DND** e "Não perturbe ativo" |
| Indisponível | Desconectado | **Não recebe chamadas de fila** | "Indisponível" |

A nota é um texto livre de até 140 caracteres, por exemplo "Almoço, volto 14h".

Por enquanto, as ausências (ausente, ocupado e ausência prolongada) continuam
recebendo chamadas de fila. Esse comportamento ainda será reavaliado.

## "Não perturbe" confirmado × provável

| | Confirmado (tag **DND**) | Provável (tag **DND?**) |
| --- | --- | --- |
| Origem | A presença do ramal está em "Não perturbe" no servidor de voz | O ramal recusou chamadas com "ocupado" estando livre |
| Quem define | Os aplicativos Sufficit (pela API de presença) ou a equipe de gestão | O próprio telefone ou aplicativo (por exemplo, o "Não perturbe" do MicroSIP) |
| O servidor sabe antes de ligar? | Sim. A fila nem oferece a chamada | Não. A fila oferece a chamada e recebe "ocupado" |
| Quando some | Quando a presença muda | Quando o ramal volta a tocar, ou 15 minutos depois da última recusa |

O "Não perturbe" de aplicativos como o MicroSIP fica só no aparelho: o servidor
recebe apenas "ocupado" e não consegue confirmar o motivo. Por isso o painel
mostra **DND?**. Nesses casos, a fila deixa o ramal fora das ofertas durante a
"espera após ramal ocupado" configurada na fila (padrão de 10 segundos) e tenta
de novo depois.

Clientes costumam ligar o "Não perturbe" sem perceber e depois relatam que "a
fila não toca". A tag **DND** ou **DND?** no card do ramal é o primeiro ponto a
verificar.

## Regras

- O estado é o mesmo em todos os servidores de voz, então não depende de onde o
  aparelho está registrado.
- "Não perturbe" e "Indisponível" tiram o ramal das ofertas de todas as filas de
  que ele participa. Não é uma pausa da fila: ao mudar a presença, ele volta a
  receber.
- Se o servidor não conseguir ler a presença, a fila oferece a chamada
  normalmente. Uma falha nunca deixa de oferecer chamada.
- No painel, o card mantém o tamanho e a cor de fundo do estado do ramal. A
  presença aparece na linha de estado do card, e o "Não perturbe" também na borda e no
  ícone.

## Exceções

- Ramais em tecnologia SIP legada não exibem a presença no painel, porque a
  presença é ligada ao código único do ramal e esses cards usam o número. O
  "Não perturbe" provável continua aparecendo.
- O "Não perturbe" de aplicativos de terceiros não é confirmado (veja acima).

## Exemplo fictício

O ramal 6001 da empresa fictícia "Clínica Exemplo" define a presença "Ausente"
com a nota "Almoço, volto 14h". No painel, o card mostra "Ausente · Almoço,
volto 14h", e a fila continua oferecendo chamadas a ele. Às 14h, a atendente
muda para "Não perturbe": o card passa a mostrar a tag **DND**, e as filas
deixam de oferecer chamadas até ela voltar para "Disponível".

## Fluxos relacionados

- [Servidores de voz](servidores-voz.md)
- [Gravação de chamadas](gravacao-chamadas.md)
- [Voltar ao índice de Telefonia](index.md)

Última revisão: 24/11/2026. Área responsável: Telefonia.
