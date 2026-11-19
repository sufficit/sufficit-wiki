# Servidores de voz — página pública

Pedido do responsável (19/11/2026): documentar os três servidores de voz na wiki.

Criada `Sufficit/Telephony/servidores-voz.md`, incluída no índice de Telefonia e citada no README.

Conferido em 19/11/2026: os três servidores (`apoint-voip`, `eveo-voip`, `google-voip`) aceitam
registro e WebSocket seguro; contatos são compartilhados e chamadas para um ramal registrado em
outro servidor são encaminhadas por ele; o perfil de navegador e o vídeo (VP8/H.264 quando o
ramal permite) estão nos três; a gravação é só de áudio. `voip.sufficit.com.br` ainda aponta
para um único servidor: o DNS com *failover* e localização foi descrito como próximo passo, a
pedido do responsável. Sem endereços IP, portas administrativas ou dados de clientes.
