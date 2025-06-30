import signal
import subprocess
import time

import requests

from config import ChatConfig, ChatMessage
from investidor import Investidor
import ollama  # type: ignore
from typing import get_args
import os
import pandas as pd

def list_files(folder_name: str):
    return [file for file in os.listdir(folder_name) if file.endswith('.txt')]

def set_investors() -> Investidor:

    documentAddress = "C:/Users/Felipe/Downloads/Overview.xlsx"
    sheet = 'Assessor'

    df = pd.read_excel(documentAddress, sheet, skiprows=3, usecols=[2, 2])

    return Investidor(df.values[11], df.values[23], df.values[8])


def read_files(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def build_config(investidor: Investidor) -> ChatConfig:
    print("== Choose your seetings ==\n")
    model_list = get_args(ChatConfig.__annotations__['model'])
    print("\nmodel list:")
    for index, model in enumerate(model_list, start=1):
        print(f"{index}. {model}")
    while True:
        try:
            choice = int(input("Choose a model by number: "))
            model_name = model_list[choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid selection\n")
    
    message = build_message(investidor)
    
    return ChatConfig(
        model=model_name,
        messages=message
    )

def build_message(investidor: Investidor) -> ChatMessage:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(BASE_DIR, "data")

    try:
        rule = read_files(os.path.join(base_path, "rules", 'rule1.txt'))
    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        profile = read_files(os.path.join(base_path, "profiles", 'profile1.txt'))
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        opportunity = read_files(os.path.join(base_path, "opportunities", 'opportunity1.txt'))
    except Exception as e:
        print(f"An error occurred: {e}")

    mensagem = (
        f"Use this information as your context: {rule}; {profile}; {opportunity}; "
        f"SELIC hoje é 15%. IPCA hoje é 4.8%. CDI hoje é 14.9%.\n"
        f"Sua tarefa: Crie um portifolio de investimentos de {investidor.patrimonioLiquido} reais para um perfil {investidor.perfil}.\n"
        f"Separe parte do valor do portifolio para reserva de emergência no valor de 10x{investidor.despesasTotais}. "
        f"A % da reserva faz parte da % total para pós-fixados.\n"
        f"Cada classe de investimento deve ter no máximo 4 ativos.\n"
        f"Liste o portifolio com os ativos escolhidos por classe e com os valores em cada ativo. Sem comentários ou observações."
    )

    return [ChatMessage(role="user", content=mensagem)]

def use_ollama(config: ChatConfig) -> str:
    try:
        response = ollama.chat(
            model=config.model,
            messages=[message.__dict__ for message in config.messages],
            stream=config.stream,
            options={"think": config.think}
        )
    except Exception as error:
        print(error)
    return response


def main():

    investidor = set_investors()
    config = build_config(investidor)
    response = use_ollama(config)
    for chunk in response:
        print(chunk['message']['content'], end='', flush=True)


if __name__ == "__main__":
    main()