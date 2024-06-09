# App Challenger

## Etapas de desenvolvimento

1. Cnpjs sejam enriquecidos em uma api, optamos pela api aberta
da receitaws(https://developers.receitaws.com.br/#/operations/queryCNPJFree). Feito !

2. Com o resultado da consulta, vamos gerar um arquivo tabulado contendo: Feito !

- CNPJ. Feito !
- data de abertura. Feito !
- nome. Feito !
- atividade_principal. Feito !
- atividade_secundaria. (caso tenha, e caso tenha mais de uma armazenar apenas a primeira) Feito !
- ultima_atualizacao. Feito !
- capital_social. Feito !

3. Sejam armazenados nos campos atividade_principal e atividade_secundaria apenas os números e não os títulos, removendo as pontuações. Feito!

4. O resultado dessa consulta deve ser armazenado em um arquivo CSV na mesma estrutura, utilizando o ; como separador.

## Partindo do CSV original contendo os CNPJs, supondo que o csv seja a tabela empresas em um banco de dados relacional, qual das datas que mais aparece?

1. Elaborada uma consulta SQL que atribua uma posição ou
classificação a cada linha, com base na quantidade de datas, ordenando as de forma
decrescente.

### O desafio deverá ser concluído até o dia 10/06/2024 segunda-feira às 12h. 

