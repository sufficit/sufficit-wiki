# Tronco tarifado: recargas, validade e compromisso

Namespace: `Sufficit.Sales`.

## Disponibilidade

As regras abaixo descrevem o modelo tarifado adotado na gestão de serviços.
A configuração de sobreposição no catálogo está disponível na versão 1.26.1106.2113 da interface, com a API correspondente.
O acesso ao lançamento depende das permissões comerciais do gestor.

## Saldo e validade

Uma recarga soma crédito ao saldo para chamadas, exibido com quatro casas decimais.
Ela não apaga o saldo anterior. O valor da compra é o valor daquela recarga, não uma
mensalidade presumida nem uma média de consumo.

A validade do serviço é informada no lançamento. Uma nova recarga substitui a
cobertura anterior: o período anterior termina antes da nova ativação, sem prolongar
um período que já venceu. Lacunas sem cobertura permanecem visíveis. A recarga rápida
usa seis meses como prazo padrão.

Mesmo com saldo positivo, o serviço é considerado vencido quando termina sua
validade. Isso não comprova, isoladamente, que houve interrupção de chamadas na central.

Cada crédito tarifado vale seis meses. A rotina semanal de revisão calcula o total
recarregado nos últimos seis meses e remove, com auditoria, o saldo excedente a esse
teto. Entre o vencimento e a revisão, pode existir saldo positivo em serviço vencido.
Evidência incompleta ou inconsistente exige análise antes do ajuste.

## Compromisso e recorrência

Sem compromisso contratado, a compra é avulsa e não cria obrigação mensal. Com
compromisso, várias recargas podem completar o valor dentro do período acordado;
a gestão indica cumprimento ou valor faltante. Um equivalente mensal não altera
um compromisso trimestral em obrigação mensal.

Recorrência e pré/pós-pago são independentes. Recorrência define repetição; pré/pós-pago
define o momento do lançamento financeiro. Validade do crédito não autoriza uma nova
compra automática. A geração de um débito não comprova pagamento.

## Consultar recargas

Na gestão de serviços, clique em **Saldo para chamadas** para abrir as recargas.
Cada linha mostra o valor e o período correspondente. O ícone de situação explica
se houve substituição dentro do prazo ou lacuna. O ícone de relatório abre o relatório
de telefonia com cliente e período selecionados. O consumo nesse intervalo não
identifica exclusivamente qual recarga foi consumida, pois o saldo é acumulado.

## Políticas genéricas de ativação

O catálogo pode configurar permitir sobreposição, impedir sobreposição ou substituir
o anterior para o mesmo cliente e tipo. A validade efetiva pertence ao lançamento.
Substituições que afetem cobertura já faturada ou recursos vinculados exigem revisão;
não há estorno automático. Alterar a configuração não reescreve o histórico.

Relacionado: [Serviços pré-pagos](servicos-pre-pagos.md).

Revisão das regras: 06/11/2026. Área: gestão de serviços e telefonia.
