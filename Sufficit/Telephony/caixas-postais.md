# Caixas postais: gravação e recebimento de recados

Namespace: `Sufficit.Telephony`

A caixa postal recebe um recado de voz de quem liga. O recado é encaminhado aos contatos de notificação configurados para aquela caixa. **O envio por WhatsApp faz parte desse funcionamento**, quando há um destinatário válido nesse canal e a integração está habilitada.

## Disponibilidade e pré-requisitos

Este guia descreve o fluxo de caixas postais com contatos de notificação. A disponibilidade das telas e dos canais depende da versão e da configuração do seu ambiente. Configurações legadas podem ter diferenças; consulte o suporte se a sua tela não corresponder ao guia.

Para receber recados, a empresa precisa ter uma caixa postal habilitada, um fluxo de atendimento que encaminhe a ligação para ela e contatos de notificação válidos. Para consultar ou alterar a configuração, é necessário acesso à empresa e permissão de gestão de telefonia.

## Como funciona

1. A ligação chega à caixa postal conforme o fluxo de atendimento configurado.
2. A pessoa deixa um recado de voz.
3. O sistema processa o recado e identifica os contatos inscritos nas notificações daquela caixa.
4. O recado é encaminhado pelos canais configurados. No WhatsApp, o envio inclui o áudio; as informações da chamada podem chegar em uma mensagem separada.

Uma caixa pode ter mais de um destinatário. O número de quem recebe o WhatsApp não é deduzido do nome da caixa, do ramal ou do telefone de quem deixou o recado.

## Para qual WhatsApp os recados são enviados?

1. No painel, selecione a empresa correta e abra os detalhes da caixa postal.
2. Consulte a seção **Contatos de notificação**.
3. Confira os contatos inscritos, o canal e o destino de cada contato. Para WhatsApp, esse destino indica quem está configurado para receber os recados.

A configuração comprova o destinatário previsto, mas não comprova que uma mensagem específica foi entregue. Se precisar verificar um envio, informe ao suporte a caixa postal e o horário aproximado da chamada.

**Não confunda com “Destino pós-gravação (Opcional)”.** Esse campo define o destino da ligação depois da gravação; não é o número de WhatsApp que recebe o recado.

## Como ouvir um recado

Quando o recado foi enviado por WhatsApp, abra a conversa que recebeu a notificação e reproduza o áudio recebido. Se houver outro canal configurado, consulte a mensagem e o anexo disponibilizados nesse canal.

Não presuma que basta ligar para o nome ou número da caixa para ouvir recados. O título de uma caixa não comprova que ela tenha um número de discagem direta, e uma entrada telefônica para **gravar** recados não é um menu para **ouvir** mensagens armazenadas. Não há, neste guia, um código de acesso ou menu por senha confirmado para essa finalidade.

Também não é possível concluir que existe uma lista de recados reproduzíveis no painel apenas porque há uma tela de configuração da caixa. Para outros meios de consulta disponíveis no seu ambiente, peça orientação ao suporte.

## Se o recado não chegar

- Confira a empresa, a caixa postal e os contatos inscritos em **Contatos de notificação**.
- Verifique se o destino e o canal estão corretos e se a caixa está habilitada.
- Uma caixa cadastrada não garante recebimento: é necessário haver um destinatário válido e uma integração operacional.
- Sem contatos válidos, não há destinatário para o envio. Dependendo da configuração do ambiente, essa condição também pode levar à desativação automática da caixa.
- Não confunda mensagem encaminhada ou enfileirada com entrega confirmada. Solicite a verificação do envio antes de concluir que o destinatário recebeu o áudio.

## Exemplo ilustrativo

Uma empresa cria a caixa “Recados do atendimento” e inscreve dois contatos de notificação: um de WhatsApp e outro de e-mail. Quando alguém deixa um recado, o sistema encaminha a notificação aos destinatários configurados. Alterar o destino pós-gravação muda o encaminhamento da ligação, não esses contatos.

## Orientação para atendimento

Ao explicar o recurso, consulte a configuração da empresa. Se não houver acesso aos contatos de notificação, informe que o destinatário ainda não foi verificado. Não afirme que a caixa não envia WhatsApp nem invente códigos ou procedimentos de acesso de outros sistemas de telefonia.

## Páginas relacionadas

- [Gravação de chamadas](gravacao-chamadas.md)
- [Telefonia](index.md)
- [Wiki Sufficit](../../README.md)

Última revisão: 28/10/2026. Área responsável: Telefonia e notificações.
