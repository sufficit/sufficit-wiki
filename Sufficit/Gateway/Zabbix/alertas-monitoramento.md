# Alertas de monitoramento por ligação e WhatsApp

Namespace: `Sufficit.Gateway.Zabbix`.

## Objetivo e disponibilidade

Receber uma ligação quando o monitoramento identificar um problema importante, com uma mensagem falada sobre o evento. O cenário pode ser de baixo volume, somente saída e um único destinatário de plantão.

A Sufficit possui uma integração Zabbix com recebimento de eventos por webhook, disparo de chamadas com conversão de texto em voz e histórico de execuções. **A ativação depende da configuração e da versão instalada no ambiente contratado.** Esta página descreve a implementação avaliada; não confirma que um acesso já esteja provisionado.

| Recurso | Situação na implementação avaliada |
| --- | --- |
| Receber alerta Zabbix e iniciar ligação com texto falado | Implementado; exige integração ativa, destinatário habilitado e configuração de chamadas. |
| Configurar webhook e ação no Zabbix pela integração | Implementado; depende de conectividade e permissão administrativa no Zabbix. |
| Consultar eventos, tentativas e resultado telefônico | Implementado; acesso sujeito às permissões da conta. |
| Confirmar o alerta apertando uma tecla | Pendente no fluxo padrão de chamadas; cadastrar uma tecla não ativa a confirmação. |
| Escolher a bina no cadastro do gateway | O campo existe, mas seu valor não é transmitido ao disparo padrão avaliado. A apresentação do número precisa ser definida na rota e testada. |
| Suprimir automaticamente alertas repetidos pela janela do gateway | A configuração existe, mas não é aplicada pelo fluxo avaliado. Controle as repetições na origem até validação de uma solução específica. |
| Enviar WhatsApp a partir do mesmo alerta | Há integração WhatsApp separada; o gateway Zabbix avaliado não realiza esse envio automaticamente. Exige integração adicional e teste. |
| Garantir um canal e teto de minutos ou gasto | Não são garantias do cadastro Zabbix; precisam constar da configuração e das condições do serviço. |

## Escolha do formato

### Integração Zabbix por webhook

O Zabbix envia o evento por HTTPS. A Sufficit inicia a ligação e reproduz o texto do alerta depois do atendimento. O monitoramento não precisa registrar um telefone SIP para usar esse fluxo.

Esta opção serve quando o monitoramento precisa também do mecanismo que realiza a chamada e fala a mensagem. SIP significa *Session Initiation Protocol*, o protocolo de sinalização usado em telefonia pela internet.

### Acesso SIP para um robô existente

Se o monitoramento já possui um robô que faz chamadas, pode-se solicitar um ramal ou tronco SIP dedicado. Nesse formato, o robô realiza a chamada e controla sua mensagem e confirmação, conforme os recursos dele e a configuração da telefonia.

A disponibilidade do ramal ou tronco e seus parâmetros dependem do provisionamento. A confirmação por tecla deve ser testada de ponta a ponta, mesmo quando o robô já a suporta.

## Pré-requisitos

- Serviço com saída para os destinos necessários e condições comerciais definidas.
- Destinatário de plantão e critérios de gravidade escolhidos pelo responsável pelo monitoramento.
- Integração habilitada, destino habilitado e configuração de chamadas associada, para usar o gateway Zabbix.
- Conta autorizada a configurar a integração. A configuração automática exige token de um usuário **Super Admin do Zabbix**; o usuário que apenas acompanha os alertas não precisa receber esse perfil.
- Conectividade do monitoramento com o endereço HTTPS da integração, ou com os serviços SIP e de áudio quando usar um robô SIP.
- Procedimento privado para cadastrar credenciais em um cofre de segredos.

## Ativação do gateway Zabbix

1. Solicite à equipe responsável a confirmação de disponibilidade no ambiente e a configuração de saída telefônica.
2. Na área **Alertas telefônicos Zabbix**, configure a integração e associe a configuração de chamadas. Cadastre e habilite o destinatário de plantão.
3. Defina a gravidade mínima que deve gerar ligações. A configuração automática permite selecionar um nível mínimo de severidade; confirme se a regra atende aos eventos que devem chamar o plantão.
4. Use o endereço de callback fornecido pela integração para configurar o webhook no Zabbix. Na configuração automática, valide a conexão e autorize a criação ou atualização do webhook e da ação pelo administrador do Zabbix.
5. Ajuste no Zabbix as regras de repetição, horários e eventos que devem gerar aviso. Não dependa somente da janela de repetição cadastrada no gateway.
6. Combine um teste com o destinatário, envie um evento fictício e confirme toque, áudio, número apresentado e resultado no histórico.
7. Libere a operação somente depois de validar as condições obrigatórias do atendimento, incluindo limites e confirmação por tecla se ela for exigida.

**Um alerta aceito não significa que houve uma ligação.** Sem destinatários habilitados ou sem configuração de chamadas, o gateway pode aceitar e registrar o evento apenas para validação. Consulte o resultado e as tentativas no histórico.

## Dados a confirmar para um acesso SIP

Use esta lista com a equipe que provisionará o serviço. Os valores são específicos do acesso contratado e devem ser entregues por canal privado quando incluírem credenciais ou dados da conta.

| Item | O que deve ser definido antes da ativação |
| --- | --- |
| 1. Formato | Ramal SIP ou tronco; somente saída; destinos permitidos e quantidade de canais simultâneos. Para baixo volume, pode-se solicitar um canal. |
| 2. Conexão | Servidor SIP, porta, transporte UDP/TCP/TLS, usuário e autenticação por registro ou por IP. |
| 3. IPs autorizados | Informar os IPs públicos do monitoramento principal e de reserva, se a autenticação ou o firewall depender deles. Testar ambos. |
| 4. Codec | Confirmar G.711 A-law ou µ-law, também chamados `alaw` e `ulaw`, e a ordem de preferência. |
| 5. Teclas | Confirmar DTMF, a sinalização das teclas durante a ligação, no modo de eventos RTP solicitado como RFC2833/RFC4733. Testar a tecla de confirmação no robô. |
| 6. Discagem | Definir o formato aceito para celular: DDD e número, código do país ou formato com zero; informar eventual prefixo de saída. Não presumir que todos sejam aceitos. |
| 7. Bina | Definir o número apresentado ao destinatário e verificar em uma chamada real antes de salvá-lo como contato do NOC. |
| 8. Limites e custo | Confirmar canais, teto de minutos ou gasto, comportamento ao atingir o teto, valor por minuto para celular e forma de tarifação. |
| 9. Áudio e firewall | Receber a faixa UDP de RTP, o protocolo que transporta o áudio, e os endereços e portas necessários. Usar os parâmetros do acesso provisionado. |
| 10. Credenciais | Combinar o cadastro da senha diretamente no cofre indicado pelo responsável. Não enviar senha por WhatsApp nem inserir credenciais nesta wiki. |

O gateway recomenda cadastrar destinos no padrão internacional E.164, com código do país, DDD e número. Isso não define o prefixo de discagem de um ramal SIP; são configurações diferentes.

Esta página não estabelece uma tarifa, uma faixa de portas universal nem um número de bina. Esses dados precisam ser confirmados no serviço entregue.

## Confirmação, repetição e limites

**Atender à ligação não comprova que uma pessoa ouviu ou reconheceu o alerta.** No fluxo padrão avaliado, o resultado de entrega se baseia no atendimento telefônico; uma caixa postal também pode atender. A tecla cadastrada na integração não é encaminhada à chamada para exigir reconhecimento.

Se o requisito for “apertar 1 para confirmar”, a ativação depende de implementar ou integrar esse comportamento e testar: atendimento sem tecla, tecla correta, tecla incorreta e ausência de resposta. Não confunda essa confirmação com o reconhecimento do evento no próprio Zabbix; a atualização automática do evento também precisa ser validada separadamente.

Os destinatários habilitados são percorridos por prioridade, e o gateway solicita um disparo para cada um. **Isso não garante escalonamento com espera até o primeiro confirmar**, nem impõe limite de um canal. Para um cenário simples, configure um destinatário e confirme o limite de simultaneidade na telefonia.

Existe proteção pontual contra disparos muito próximos ao mesmo destino no serviço de chamadas. Ela não substitui política de repetição de alertas, fila de escalonamento ou teto financeiro. Não presuma rediscagem automática até confirmação: defina e teste essa política antes da operação.

## WhatsApp e usuário observador

A Sufficit possui integração WhatsApp via Quepasa, separada do gateway Zabbix. Na implementação avaliada, receber um alerta Zabbix não envia automaticamente uma mensagem WhatsApp.

Uma saída dedicada a esses avisos precisa de canal configurado, credencial de automação, destinatários e uma integração que faça o envio. Confirme com a equipe responsável a disponibilidade, os limites e as condições do canal antes da ativação.

O requisito recomendado é separar a automação da conta humana: a credencial do robô executa os envios autorizados, enquanto o usuário do painel apenas consulta. **Essa separação precisa ser verificada nas permissões efetivas do ambiente.** Acesso à tela, isoladamente, não comprova que a conta seja somente leitura; o teste deve incluir a tentativa de alterar configurações e iniciar envios.

Teste o canal WhatsApp separadamente da voz. A entrega de uma mensagem não equivale à confirmação do alerta pela pessoa, e a disponibilidade de um canal não garante a do outro.

## Falhas e recuperação

| Situação | Como proceder |
| --- | --- |
| Evento aceito, mas sem chamada | Conferir destinatários habilitados, configuração de chamadas e resultado da execução. |
| Ocupado, sem atendimento ou tempo esgotado | Consultar a tentativa; verificar o destino e aplicar a política de nova tentativa definida para o monitoramento. |
| Falha de rota ou rejeição telefônica | Solicitar revisão do acesso e da saída para o destino à equipe responsável. |
| Ligação atendida, mas sem áudio | Testar codec e conectividade RTP no acesso provisionado; o atendimento sozinho não valida o áudio. |
| Repetições gerando excesso de ligações | Rever ações e repetição no Zabbix; confirmar limites de chamadas e gasto. |
| Falha na configuração automática | Conferir endereço da API, conectividade, token válido e permissão Super Admin no Zabbix. |
| WhatsApp não enviado | Verificar a integração adicional e o canal WhatsApp; o histórico de voz não comprova envio de mensagem. |

Ao solicitar suporte, informe o horário do teste e o identificador da execução pelo canal privado de atendimento. Não publique tokens, senhas nem dados reais do evento em exemplos públicos.

## Exemplo ilustrativo

Uma empresa fictícia quer avisar o plantão quando um equipamento crítico ficar indisponível. Ela cadastra um único destinatário, configura a ação do Zabbix e envia um evento de teste com a mensagem “Alerta de teste: equipamento de demonstração indisponível”.

O teste deve demonstrar que a ligação toca, a mensagem pode ser ouvida, a bina corresponde ao número combinado e o histórico registra o resultado. Se a confirmação por tecla for obrigatória, o atendimento da ligação sozinho não aprova o teste. O WhatsApp, quando contratado e integrado, exige uma verificação adicional de envio e recebimento.

## Checklist de aceite

- Formato de integração escolhido e parâmetros entregues.
- Saída para celular, áudio e bina testados.
- Monitoramento principal e reserva testados, quando aplicável.
- Um canal ou outra simultaneidade acordada efetivamente configurada.
- Tarifa, teto e comportamento ao atingir limites confirmados.
- Política de repetição e nova tentativa validada.
- Confirmação por tecla testada, se exigida.
- WhatsApp testado separadamente, se incluído.
- Conta observadora verificada sem permissões de alteração ou envio.
- Segredos cadastrados pelo procedimento privado combinado.

## Navegação e revisão

- [Integrações Zabbix](index.md).
- [Integrações Sufficit](../index.md).
- [Índice geral da wiki](../../../README.md).

Última revisão: **14/10/2026**, por conferência da implementação. Área responsável: Integrações e Telefonia. Não foi realizado teste em ambiente de cliente nesta revisão.
