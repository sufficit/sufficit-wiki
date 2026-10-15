# Diagnóstico do certificado da wiki

Falha TLS confirmada: certificado apresentado não cobre wiki.sufficit.com.br. API Pages retorna certificado nulo e HTTPS obrigatório desativado.

O CNAME público aponta para sufficit.github.io. Consultas ao autoritativo Route53 e aos resolvedores Google e Cloudflare confirmam o registro. A resolução leva aos endereços GitHub Pages. A consulta CAA permite letsencrypt.org.

Removido e recadastrado o domínio na API Pages para reiniciar o provisionamento, conforme a orientação oficial do GitHub. O domínio final permaneceu wiki.sufficit.com.br.

O diagnóstico de domínio do GitHub retornou dns_resolves=false, InvalidDNSError e Dnsruby::NXDomain. Isso contrasta com as consultas públicas e indica provável cache negativo anterior à criação do registro. A zona tem TTL de SOA de 900 segundos; não é uma garantia do prazo de atualização do GitHub.

Certificado e HTTPS obrigatório continuam pendentes de nova validação pelo GitHub. Não ignorar a validação TLS como solução. Nenhuma alteração DNS adicional foi feita.

Fonte: https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https

Registro salvo localmente; o plano mantém o checkpoint de validação em andamento.
