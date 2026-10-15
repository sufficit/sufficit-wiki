# Certificado HTTPS da wiki corrigido

Concluída a ativação de HTTPS para wiki.sufficit.com.br.

## Diagnóstico e ação

Na tentativa anterior, o diagnóstico GitHub ainda retornava NXDomain. Nesta conferência, o próprio GitHub confirmou domínio válido, CNAME correto, ausência de erro CAA e elegibilidade para HTTPS, mas a API de ativação retornou que o certificado não existia.

O domínio foi removido e recadastrado uma vez com a resolução DNS já validada. O GitHub passou a informar certificado aprovado. Ativado HTTPS obrigatório. Nenhuma alteração DNS adicional foi necessária.

## Validação

- API Pages: certificado em estado approved, domínio wiki.sufficit.com.br, validade até 13/01/2027 e https_enforced=true.
- Conexão TLS com validação padrão de cadeia e hostname: aprovada. SAN contém wiki.sufficit.com.br; emissor Lets Encrypt YR1.
- Página de alertas por HTTPS: HTTP 200, sem ignorar a validação do certificado.
- Mesma URL por HTTP: redirecionamento 301 para HTTPS.
- Plano concluído e removido; este registro substitui a pendência operacional registrada no diagnóstico anterior.

[Página validada](https://wiki.sufficit.com.br/Sufficit/Gateway/Zabbix/alertas-monitoramento.html).

[Procedimento oficial aplicado](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https).
