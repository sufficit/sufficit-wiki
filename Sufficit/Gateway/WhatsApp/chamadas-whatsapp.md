# Chamadas recebidas pelo WhatsApp

Namespace: `Sufficit.Gateway.WhatsApp`

## Objetivo

Receber na central telefônica as ligações feitas para um número de WhatsApp da
empresa, como se fossem ligações de uma linha telefônica, e escolher para onde
elas seguem no plano de discagem.

## Disponibilidade

Disponível para números conectados pelo QuePasa e para números oficiais da Meta,
no painel em **WhatsApp › Chamadas e conexões**. A ativação depende de o número
estar conectado e de a empresa ter permissão para alterar o plano de discagem.

## Pré-requisitos

- Número de WhatsApp conectado (QR Code ou código de pareamento) ou número
  oficial compartilhado com a Sufficit.
- Permissão de edição do plano de discagem da empresa.
- Um destino sem menu de teclas (veja as regras abaixo).

## Passos

1. Abra **WhatsApp** no painel e localize o número na lista.
2. Use **Editar destino** e escolha o destino das chamadas.
3. Salve. A partir daí, as chamadas de WhatsApp para esse número entram na
   central e seguem o destino escolhido.

Um número que já atende mensagens pelo Hermes pode receber chamadas também: o
mesmo número passa a ter a rota de chamadas, e as mensagens continuam chegando
normalmente no Hermes.

## Regras

### Chamadas de WhatsApp não enviam teclas (DTMF)

Hoje, quem liga pelo WhatsApp não consegue digitar opções durante a chamada
(tons DTMF). Por isso:

- **Não aponte** a chamada para uma URA, menu de opções ou qualquer etapa que
  espere o cliente digitar. Quem liga fica preso na mensagem até o tempo acabar.
- **Use** uma condição de horário de expediente: dentro do horário, a chamada vai
  direto para uma fila (ou ramal); fora do horário, para um anúncio e, se
  desejar, para uma caixa postal.
- Confira se a fila também não depende de tecla (por exemplo, "digite 1 para
  deixar recado").

O destino do número de telefone da empresa pode continuar com URA: a regra vale
para o destino da rota do WhatsApp.

### Quem atende a chamada

Na configuração padrão, a central atende a chamada de WhatsApp e a encaminha ao
destino; o celular do número deixa de tocar para essas ligações. Se a empresa
preferir que o celular continue tocando junto com a central, isso pode ser
ajustado pelo suporte.

### Aparelhos conectados

O WhatsApp entrega chamadas a no máximo quatro aparelhos conectados além do
celular principal. Com mais aparelhos, parte das ligações toca só no celular e
não chega à central, mesmo com as mensagens funcionando. Desconecte os aparelhos
sem uso em **Configurações › Dispositivos conectados** no celular.

## Exceções

- **Número já cadastrado em outra empresa:** o painel recusa o cadastro; peça a
  transferência ao suporte.
- **Número desconectado:** use **Reconectar** para gerar novo QR Code ou código
  de pareamento; a rota é mantida.
- **Chamada não chega:** use **Diagnosticar conexão** e confira a quantidade de
  aparelhos conectados.

## Exemplo fictício

A "Clínica Exemplo" atende mensagens no Hermes pelo número +55 11 90000-0000 e
quer receber as ligações desse WhatsApp. O destino escolhido é a condição de
horário "Expediente WhatsApp" (segunda a sexta, 08:00 às 18:00): dentro do
horário, a ligação entra direto na fila "Recepção"; fora dele, toca um anúncio
e segue para a caixa postal "Recados".

## Fluxos relacionados

- [Caixas postais](../../Telephony/caixas-postais.md)
- [Filas: ramal ocupado, sem resposta e sem aparelho](../../Telephony/filas-ramal-ocupado.md)
- [Voltar ao índice do WhatsApp](index.md)

Última revisão: 25/11/2026. Área responsável: Telefonia.
