import os
import subprocess

import ollama
import pandas as pd

from config import ChatConfig, ChatMessage
from investidor import Investidor


def list_files(folder_name: str):
    return [file for file in os.listdir(folder_name) if file.endswith('.txt')]


def set_investors() -> Investidor:
    documentAddress = "C:/Users/Felipe/Downloads/Overview.xlsx"
    sheet = 'Assessor'

    df = pd.read_excel(documentAddress, sheet, skiprows=3, usecols=[2, 2])

    investidor =  Investidor(df.values[11][0], df.values[23][0], df.values[8][0])

    return investidor



def read_files(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def build_config(investidor: Investidor) -> ChatConfig:

    return ChatConfig(
        model="gemma3:27b",
        messages=build_message(investidor)
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
        f"Use this information as your context: {rule}. {profile}. {opportunity}. "
        f"SELIC today is at 15%. IPCA today is at 4.8%. CDI today is at 14.9%.\n"
        f"Your task: Create an investments portfolio for a {investidor.perfil} profile with {investidor.patrimonioLiquido} reais of net worth,"
        f" following the proportions and using the investments given in the context part, separating"
        f"part of the portfolio for an emergency reserve of 10x{investidor.despesasTotais} reais. "
        f"Each investment class should have no more than 4 assets. "
        f"Show me the portfolio with the chosen assets for each investment class and with the value in reais (R$) for each class and asset. No comments and no observations."
    )

    return [ChatMessage(role="user", content=mensagem)]


def use_ollama(config: ChatConfig) -> str:

    try:
        response = ollama.chat(
            model=config.model,
            messages=[message.__dict__ for message in config.messages],
            stream=config.stream,
            keep_alive=-1,
            options={"think": config.think}
        )
    except Exception as error:
        print(error)

    return response

def main():

    ollama_server = subprocess.Popen(['ollama', 'serve'], stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL)

    investidor = set_investors()
    config = build_config(investidor)
    print('loading task 1')
    response = use_ollama(config)
    for chunk in response:
        print(chunk['message']['content'], end='', flush=True)

    kill_ollama = subprocess.Popen(['ollama', 'stop', config.model])
    kill_ollama.wait()

if __name__ == "__main__":
    main()
