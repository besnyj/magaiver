import requests
import classes


def getSelic():
    response = requests.get(classes.Indexadores.selic_url)
    data = response.json()
    return data

def getIpca():
    response = requests.get(classes.Indexadores.ipca_url)
    data = response.json()
    return data

def getCdi():
    response = requests.get(classes.Indexadores.cdi_url)
    data = response.json()
    return data
