# App Challenger

## Informações:
O programa foi feito em uma maquina virtual no sistema operacional linux.
Primeiramente criei um ambiente virtual com as dependências importantes para a execução, depois manipulei o dados_iniciais.csv para a forma de dicionário que é um json(dict_cnpjs).
Depois coloquei o request na função consultar_cnpj que é chamada ao percorremos os valores de dict_cnpjs e armazenamos dentro da lista resultados que é transformada em dataframe com a função nativa do pandas e depois a transformamos em csv separado por virgulas. Os erros foram capturados pelo modulo erros.py. 

## Execução do programa: 

1. Ative o ambiente virtual: source .venv/bin/activate

2. execute python3 app.py

## Feedback:
O programa foi feito no paradigma orientado a objeto, estudando mais sobre a chamadas de APIs entendo que o paradigma funcional seria mais adequado, sucinto, performatico e replicável em sistemas de computação distribuida. Apesar disso gostei muito do desáfio e irei desenvolver uma versão funcional atualizada em seguida. Obrigado pelo teste =D.
