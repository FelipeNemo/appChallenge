from erros import *
import pandas as pd
import requests
import time
import re


# Tratamento de dados_iniciais.csv
base_cnpj = pd.read_csv('dados_inicias.csv', sep= ',', header=None,skiprows=1)

cnpjs = base_cnpj.iloc[:, 0]

dict_cnpjs = cnpjs.to_dict()

try:

    # Função para extrair apenas os números da atividade, removendo pontuações
    def extrair_codigo_atividade(atividade):
        if atividade:
            return re.sub(r'\D', '', atividade['code'])
        return ""

    # Função para consultar a API da ReceitaWS
    def consultar_cnpj(cnpj):
        cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            cnpj_info = {
                "CNPJ": data.get('cnpj', ''),
                "Data de Abertura": data.get('abertura', ''),
                "Nome": data.get('nome', ''),
                "Atividade Principal": extrair_codigo_atividade(data.get('atividade_principal', [])[0] if data.get('atividade_principal') else None),
                "Atividade Secundaria": extrair_codigo_atividade(data.get('atividades_secundarias', [])[0] if data.get('atividades_secundarias') else None),
                "Ultima Atualizacao": data.get('ultima_atualizacao', ''),
                "Capital Social": data.get('capital_social', '')
            }
            return cnpj_info
        else:
            raise ErroDeRequisicao(f"Ocorreu um erro ao fazer a requisição")
        

    
    dict_cnpjs = cnpjs.to_dict()

    resultados = []

    # Iterar sobre o dicionário de CNPJs e consultar a API
    for index, cnpj in dict_cnpjs.items():
        resultado = consultar_cnpj(cnpj)
        if resultado:
            resultados.append(resultado)
        else:
            raise ErroDeConsulta(f"Erro ao consultar CNPJ {cnpj}")
        
        time.sleep(20)


        df_resultados = pd.DataFrame(resultados)
        print(df_resultados)

    print("Consulta finalizada.")

except ErroDeRequisicao as e:
    print(e)

except ErroDeConsulta as e:
    print(e)