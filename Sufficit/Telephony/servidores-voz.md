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
| Chamada para o ramal | Pode chegar por qualquer servidor. Se o aparelho estiver registrado em outro, o servidor que recebeu a chamada a encaminha pelo servidor do registro, o único caminho que atravessa o NAT do aparelho. Veja [Áudio das chamadas encaminhadas](#áudio-das-chamadas-encaminhadas). |
| Gravação e histórico | Ficam no servidor que recebeu a chamada, mesmo quando ela foi encaminhada. |
| Softphone do navegador | Recebe e faz chamadas em qualquer servidor, com o perfil próprio para navegador (áudio criptografado). |
| Vídeo | Os três servidores repassam vídeo entre aparelhos, sem gravar o vídeo. Veja [Chamadas de vídeo](#chamadas-de-vídeo). |

### Áudio das chamadas encaminhadas

Numa chamada encaminhada, o servidor do registro faz só o "chamar" do aparelho (a sinalização). Por padrão, depois que o aparelho atende, o áudio passa a ir **direto** entre o aparelho e o servidor que recebeu a chamada, sem passar pelo servidor do registro. Isso reduz atraso e evita uma volta a mais pela internet. Gravação, histórico e recursos da chamada continuam no servidor que recebeu a chamada.

| Modo | Caminho do áudio | Quando usar |
| --- | --- | --- |
| Direto (padrão) | Aparelho ↔ servidor que recebeu a chamada | A maioria dos aparelhos e redes. |
| Pelo servidor do registro | Aparelho ↔ servidor do registro ↔ servidor que recebeu a chamada | Quando o modo direto deixa a chamada muda ou com áudio num sentido só (cenários abaixo). |

O modo direto só se aplica a aparelhos e softphones comuns. O softphone do navegador sempre usa o caminho pelo servidor do registro. Chamadas em que o aparelho está registrado no mesmo servidor que recebeu a chamada não são encaminhadas e não mudam.

#### Quando o modo direto pode falhar

O servidor de voz não consegue perceber sozinho que o áudio não chegou: para ele, a chamada foi atendida normalmente. Os casos conhecidos dependem da rede ou do aparelho do cliente:

- **Firewall que libera só um servidor:** a rede da empresa permite tráfego de voz apenas para o servidor em que o aparelho se registra. No modo direto o áudio vem de outro servidor e é bloqueado.
- **Roteador com SIP ALG:** o recurso "SIP ALG" de alguns roteadores reescreve a sinalização e pode estragar a mensagem que muda o destino do áudio. O aparelho continua mandando o áudio para o servidor antigo.
- **Aparelho que não aceita mudar o destino do áudio** depois de atender (alguns adaptadores de telefone analógico e firmwares antigos).
- **NAT restritivo ou CGNAT da operadora:** a passagem aberta para um servidor não vale para outro endereço, e o áudio do segundo servidor é descartado.

Sintoma típico: a chamada é atendida, mas um dos lados (ou os dois) não ouve, e só nas ligações que chegam por um servidor diferente daquele em que o aparelho está registrado.

#### Ajuste por ramal ou por cliente

Nesses casos, o suporte pode configurar o modo **pelo servidor do registro**:

- **por ramal:** só o aparelho com problema;
- **por cliente:** todos os ramais do cliente, típico de firewall corporativo.

O ajuste vale para as próximas ligações, sem reiniciar o aparelho. Ainda não há opção para isso no painel: peça ao suporte, informando o ramal e um exemplo de ligação com o problema. Antes, confira se a opção **CGNAT** do ramal está ligada (veja [Exceções](#exceções)).

### Chamadas de vídeo

O servidor de voz não converte vídeo, apenas repassa. Os dois lados precisam ter um codec de vídeo em comum (VP8 ou H.264).

- Para um ramal fazer ou receber vídeo, VP8 e/ou H.264 precisam estar marcados nos codecs do ramal, no painel.
- No softphone do navegador, o vídeo só é oferecido quando o ramal permite VP8 ou H.264. Sem essa opção, o ramal continua apenas com áudio.
- A gravação de chamadas grava somente o áudio. Veja [Gravação de chamadas](gravacao-chamadas.md).

## Exceções

- **Áudio ou vídeo num sentido só:** um aparelho atrás de NAT pode não receber a mídia enquanto o ajuste de NAT (opção **CGNAT** do ramal, no painel) estiver desligado. Ligue a opção e faça uma nova ligação; a chamada em curso não muda.
- **Chamada muda só quando encaminhada entre servidores:** veja [Quando o modo direto pode falhar](#quando-o-modo-direto-pode-falhar) e peça ao suporte o ajuste por ramal ou por cliente.
- **Servidor indisponível:** quando o endereço padrão tiver o redirecionamento automático, o aparelho voltará a se registrar em outro servidor. Um aparelho fixado num servidor específico fica sem registro até esse servidor voltar.
- **Softphone do navegador fixado num servidor:** a escolha fica em **Configurações › Diagnóstico › Servidor de voz** e é só para testes. O normal é **Padrão (voip.sufficit.com.br)**.

## Exemplo ilustrativo

Um ramal fictício está registrado no `eveo-voip`. Uma ligação de fora chega pelo `google-voip`. O `google-voip` encaminha a chamada pelo `eveo-voip`, o aparelho toca, e a gravação e o histórico da chamada ficam no `google-voip`. Depois do atendimento, o áudio vai direto entre o aparelho e o `google-voip`. Se a empresa desse ramal só liberar tráfego para o `eveo-voip`, o suporte ajusta o ramal para o modo pelo servidor do registro, e o áudio passa a ir pelo `eveo-voip`.

## Páginas relacionadas

- [Gravação de chamadas](gravacao-chamadas.md)
- [Tronco individual](tronco-individual.md)
- [Voltar à Telefonia](index.md)

Última revisão: 21/11/2026. Área responsável: Telefonia.
