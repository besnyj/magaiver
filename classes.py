import sqlite3


class Models:
    model1 = 'gemma3:27b'
    model2 = 'gemma3:12b'
    model3 = 'gemma2:27b'
    model4 = 'mistral-small3.1:24b'
    deepseek = 'deepseek-r1:32b'
    qwen = 'qwen3:32b'
    phi = 'phi4-reasoning:14b'


class Documentos:
    oportunidades = open("oportunidades.txt")
    oportunidades = oportunidades.read()

    riskProfile = open("C:/Users/Felipe/Downloads/riskprofile.txt")
    riskProfile = riskProfile.read()


class Databases:
    database = 'data.db'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

class Indexadores:
    selic_url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=json'
    cdi_url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json&dataInicial=24/06/2015'
    ipca_url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json'
