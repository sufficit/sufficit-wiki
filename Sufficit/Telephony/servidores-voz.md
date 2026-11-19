# Servidores de voz

Namespace: `Sufficit.Telephony`

A telefonia Sufficit roda em três servidores de voz, em locais diferentes. Esta página explica qual endereço usar, o que cada servidor faz e o que acontece quando um aparelho está registrado em um servidor e a chamada chega por outro.

## Disponibilidade

- Os três servidores de voz estão em operação: `apoint-voip`, `eveo-voip` e `google-voip` (todos em `sufficit.com.br`).
- O endereço padrão para aparelhos e aplicativos é `voip.sufficit.com.br`. Ele será um nome com redirecionamento automático (*failover*) e escolha do servidor mais próximo, feito pelo DNS. Até essa mudança, ele aponta para um único servidor.

## Qual endereço usar

Use sempre `voip.sufficit.com.br` na configuração de aparelhos, softphones e aplicativos. Os dados exatos de cada aparelho (porta, transporte, usuário) aparecem no painel, em **Ramal › Conectar um aparelho**.

Os nomes de cada servidor (`apoint-voip`, `eveo-voip`, `google-voip`) servem para testes e diagnóstico. Fixar um aparelho num servidor específico tira dele o redirecionamento automático do endereço padrão.

## Regras

| Assunto | Como funciona |
| --- | --- |
| Registro | O aparelho se registra no servidor que atender o endereço configurado. O registro fica visível para os três servidores. |
| Chamada para o ramal | Pode chegar por qualquer servidor. Se o aparelho estiver registrado em outro, o servidor que recebeu a chamada a encaminha pelo servidor do registro, o único caminho que atravessa o NAT do aparelho. |
| Gravação e histórico | Ficam no servidor que recebeu a chamada, mesmo quando ela foi encaminhada. |
| Softphone do navegador | Recebe e faz chamadas em qualquer servidor, com o perfil próprio para navegador (áudio criptografado). |
| Vídeo | Os três servidores repassam vídeo entre aparelhos, sem gravar o vídeo. Veja [Chamadas de vídeo](#chamadas-de-vídeo). |

### Chamadas de vídeo

O servidor de voz não converte vídeo, apenas repassa. Os dois lados precisam ter um codec de vídeo em comum (VP8 ou H.264).

- Para um ramal fazer ou receber vídeo, VP8 e/ou H.264 precisam estar marcados nos codecs do ramal, no painel.
- No softphone do navegador, o vídeo só é oferecido quando o ramal permite VP8 ou H.264. Sem essa opção, o ramal continua apenas com áudio.
- A gravação de chamadas grava somente o áudio. Veja [Gravação de chamadas](gravacao-chamadas.md).

## Exceções

- **Áudio ou vídeo num sentido só:** um aparelho atrás de NAT pode não receber a mídia enquanto o ajuste de NAT (opção **CGNAT** do ramal, no painel) estiver desligado. Ligue a opção e faça uma nova ligação; a chamada em curso não muda.
- **Servidor indisponível:** quando o endereço padrão tiver o redirecionamento automático, o aparelho voltará a se registrar em outro servidor. Um aparelho fixado num servidor específico fica sem registro até esse servidor voltar.
- **Softphone do navegador fixado num servidor:** a escolha fica em **Configurações › Diagnóstico › Servidor de voz** e é só para testes. O normal é **Padrão (voip.sufficit.com.br)**.

## Exemplo ilustrativo

Um ramal fictício está registrado no `eveo-voip`. Uma ligação de fora chega pelo `google-voip`. O `google-voip` encaminha a chamada pelo `eveo-voip`, o aparelho toca, e a gravação e o histórico da chamada ficam no `google-voip`.

## Páginas relacionadas

- [Gravação de chamadas](gravacao-chamadas.md)
- [Tronco individual](tronco-individual.md)
- [Voltar à Telefonia](index.md)

Última revisão: 19/11/2026. Área responsável: Telefonia.
