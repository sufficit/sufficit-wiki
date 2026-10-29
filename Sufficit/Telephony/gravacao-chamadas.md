# Gravação de chamadas

Namespace: `Sufficit.Telephony`

As chamadas atendidas pelos ramais da empresa são gravadas automaticamente. A gravação vem **ligada por padrão** em todo ramal e só deixa de acontecer quando a própria empresa a desliga naquele ramal.

## Disponibilidade e pré-requisitos

Disponível na telefonia Sufficit. A opção por ramal está na tela de detalhes do ramal do novo painel; ambientes com telas legadas podem exibir a mesma opção no cadastro antigo do ramal. Consulte o suporte se a sua tela não corresponder a este guia.

Para ligar ou desligar a gravação de um ramal, é necessário acesso à empresa e permissão de telefonia dessa empresa. Não é possível alterar ramais de outra empresa.

## O que é gravado

| Situação | Gravada? |
| --- | --- |
| Ligação recebida diretamente no ramal e atendida | Sim |
| Ligação de fila de atendimento atendida por um ramal | Sim |
| Ligação interna entre ramais | Sim |
| Ligação feita pelo ramal para números externos | Sim |
| Ligação transferida ou capturada por outro ramal | Sim, também na ponta de quem recebeu |
| Ligação que só tocou e não foi atendida | Não há conversa a gravar |
| Ramal com a gravação desligada pela empresa | Não |

O áudio é registrado apenas a partir do momento em que a conversa é estabelecida. O tempo de espera e o toque não fazem parte da gravação.

## Ligar ou desligar a gravação de um ramal

1. Acesse **Telefonia › Ramais & Chamadas › Extensões** e abra o ramal desejado.
2. Na tela **Ramal**, use a opção **Gravação**.
3. Aguarde a confirmação na tela. Se a alteração não puder ser aplicada, a opção volta ao estado anterior e uma mensagem é exibida.

A mudança passa a valer para as próximas ligações, em geral em poucos segundos. Ligações em andamento não são alteradas.

Toda alteração fica registrada com quem alterou, quando e os valores anterior e novo. Esse registro é mantido por cinco anos.

## Regras

- **Padrão:** ramal novo nasce com a gravação ligada.
- **Falha temporária:** se, no momento da ligação, não for possível confirmar a preferência do ramal, a ligação é gravada. A regra privilegia não perder gravações.
- **Prazo de guarda:** cada gravação é mantida por **um ano** e excluída automaticamente depois disso. Não há prorrogação nem recuperação após a exclusão.
- **Consulta:** as gravações são ouvidas no histórico de **Chamadas**. A gravação pode não aparecer imediatamente após o fim da ligação.
- **Armazenamento:** as gravações ficam em armazenamento em nuvem, fora dos servidores de telefonia. O acesso é feito pelo produto, conforme as permissões da empresa.

## Exceções e ajuda

- Uma ligação atendida que não aparece com gravação no histórico deve ser informada ao suporte com data, hora e números envolvidos.
- Se a empresa precisar guardar gravações por mais de um ano, deve baixá-las antes do prazo de exclusão.
- Escutas de supervisão não geram uma gravação separada; a conversa acompanhada já é gravada no ramal atendido.

## Exemplo ilustrativo

Uma empresa fictícia decide não gravar o ramal da recepção. A gestora abre o ramal em **Extensões**, desliga **Gravação** e vê a confirmação. A partir das próximas ligações, as conversas desse ramal deixam de ser gravadas, enquanto os demais ramais continuam gravando. O registro de auditoria guarda quem fez a mudança e quando.

## Páginas relacionadas

- [Caixas postais: gravação e recebimento de recados](caixas-postais.md)
- [Telefonia](index.md)
- [Wiki Sufficit](../../README.md)

Última revisão: 29/10/2026. Área responsável: Telefonia.
