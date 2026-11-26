# Saudação da fila de espera

Namespace: `Sufficit.Telephony`

A saudação apresenta o atendimento antes de os ramais começarem a tocar. A fila registra a entrada assim que recebe a chamada. O tempo total na linha inclui a saudação, a espera e a conversa, quando houver atendimento.

## Configurar o áudio

Para editar uma fila, é preciso ter permissão para gerenciar sua telefonia. Use um áudio publicado e disponível na lista da fila.

1. Abra **Filas**, escolha a fila e entre na edição.
2. Na etapa de áudio, selecione o arquivo em **Saudação de entrada**.
3. Confira a **Espera máxima**, salve e faça uma chamada de teste.

## Contar a espera após a saudação

As duas opções abaixo estão em validação. A disponibilidade depende da versão do editor e do serviço de filas.

- **Contar a espera após a saudação** inicia o prazo quando o áudio termina ou é pulado. Se a reprodução falhar, a fila inicia a espera assim que retoma o fluxo. Com a opção desativada, o relógio começa na entrada e o áudio usa parte do prazo.
- **Permitir pular a saudação com qualquer tecla** interrompe o áudio e mantém a chamada na fila. Depois da saudação, voltam a valer as teclas de saída e de menu configuradas.

Exemplo ilustrativo com a primeira opção ligada. Uma saudação de 4 segundos e uma espera máxima de 15 segundos permitem até 19 segundos entre a entrada e o fim da espera. Se a pessoa pular o áudio após 1 segundo, a fila começa a contar os 15 segundos nesse ponto.

## O que acompanhar

Separe **tempo desde a entrada na fila** de **espera após a saudação**. O primeiro mostra quanto a pessoa aguardou desde que entrou. O segundo ajuda a medir a espera quando os ramais já podem tocar. Se a entrada tiver apenas um canal, a saudação também ocupa esse canal.

Um anúncio colocado antes da fila pertence ao plano de entrada. O áudio toca antes de o sistema registrar a entrada na fila. Use a saudação da própria fila quando precisar medir a entrada antes de tocar o áudio.

- [Chamadas simultâneas no 0800](chamadas-simultaneas-0800.md)
- [Filas: ramal ocupado, sem resposta e sem aparelho](filas-ramal-ocupado.md)

Última revisão em 26/11/2026. Área responsável pela página: Telefonia.
