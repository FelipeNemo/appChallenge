SELECT data_inicial, COUNT(*) AS quantidade
FROM empresas
GROUP BY data_inicial
ORDER BY quantidade DESC
LIMIT 1;
