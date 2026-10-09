# Serviços pré-pagos, limites e renovação

Namespace: `Sufficit.Sales`.
Disponibilidade: **em validação**. O backend possui implementação e testes isolados; a integração ainda depende de instalação, configuração e piloto. Esta página não afirma disponibilidade para clientes nem define o catálogo comercial definitivo.
Última revisão das regras: 06/10/2026. Área responsável: Serviços.

O serviço pré-pago permite comprar um período de uso com capacidades e franquias. Cada conta possui seu próprio contrato: um cliente pode ter várias contas cobradas separadamente. Serviços decide oferta e preço, Checkout confirma o pagamento e a aplicação utiliza os direitos autorizados.

## Contratação e pagamento

1. Um gestor associa a conta a um contrato pré-pago ativo e configura as ofertas permitidas.
2. O administrador da conta solicita uma compra e acompanha seu processamento.
3. Quando a cotação fica pronta, abre o link do Checkout e confere valor e validade.
4. O recebimento confirmado autoriza os direitos; a aplicação os recebe por reconciliação assíncrona.

Uma solicitação aceita, um pagamento ainda pendente ou o retorno do navegador não liberam franquias. A mesma compra não deve ser repetida com outra identidade quando seu resultado estiver incerto. A integração inicial oferece APIs e reaproveita o acesso ao Checkout; não há nova tela de catálogo declarada nesta fase.

## Duração e limites

A oferta define ciclo mensal ou anual. Na implementação inicial, a primeira cobertura começa no recebimento confirmado, e uma renovação antecipada começa após a última cobertura paga. Datas usam UTC, meses reais de calendário e fim exclusivo. Na oferta anual, a franquia é concedida para o período anual; não existe reset mensal implícito.

Capacidade é a quantidade simultânea de recursos permitidos. Franquia representa unidades consumíveis. O saldo de franquia não utilizado expira; não acumula. Adicionais vencem junto com o plano vigente. Métricas, preços e pacotes definitivos serão definidos posteriormente.

Ao atingir um limite, somente a operação dependente é bloqueada e pode exigir compra adicional. Recursos existentes e histórico são preservados. Esgotamento não suspende automaticamente o login. A gestão pode aplicar suspensão manual dos direitos; pagar uma compra não remove essa suspensão.

## Renovação

A renovação automática, quando habilitada no contrato associado, prepara uma nova compra antes do vencimento e disponibiliza um link de pagamento. **Não representa débito automático.** A antecedência é configurável; o padrão inicial é sete dias.

Pagar antecipadamente agenda o próximo período e não permite gastar sua franquia antes do início. Sem recebimento confirmado, não existe nova cobertura. Uma indisponibilidade temporária de integração preserva direitos já autorizados até sua validade; a reconciliação recupera atualizações pendentes.

## Upgrade, downgrade e adicionais

Upgrade entra em vigor após pagamento confirmado. Dentro do mesmo ciclo, cobra a diferença positiva de preço proporcional ao tempo restante. O vencimento é mantido e o consumo anterior não é zerado. A franquia extra incluída no upgrade também é proporcional ao tempo restante, arredondada para baixo em unidades inteiras.

Exemplo fictício: pacote vigente de R$ 100, novo pacote de R$ 200, período com metade do tempo restante: upgrade de R$ 50. Um segundo upgrade compara com o pacote já atualizado.

Downgrade fica agendado para a próxima compra de renovação e preserva os períodos já pagos. Não gera crédito automático. Trocar entre mensal e anual utiliza renovação. Um adicional de consumo é cobrado pelas unidades completas; um adicional de capacidade temporária utiliza proporcionalidade. Ambos expiram com a cobertura vigente.

O Checkout exige valor mínimo de R$ 5 nesta integração. Uma diferença proporcional abaixo desse mínimo é rejeitada; não é aumentada silenciosamente nem concede direitos gratuitamente.

## Pendências e recuperação

Pagamento confirmado que não puder ser aplicado com segurança exige revisão da gestão. Não faça outra compra para tentar resolver uma divergência financeira. Expiração, estorno e contestação são situações diferentes; a política de revogação e estorno ainda está pendente nesta fase.

A medição de cada operação de IA ou mensagens será integrada quando suas métricas comerciais forem definidas. Testes isolados não comprovam implantação ou integração completa em uma instalação. O piloto deve validar contratos distintos para duas contas, confirmação de recebimento, limites, vencimento e recuperação de falhas antes da ativação comercial.

[Voltar ao domínio Serviços](index.md) · [Índice da wiki](../../README.md)
