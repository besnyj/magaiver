import os
from .format import format_output

import ollama
import pandas as pd

from .config import ChatConfig, ChatMessage
from .investidor import Investidor


def list_files(folder_name: str):
    return [file for file in os.listdir(folder_name) if file.endswith('.txt')]


def set_investors(formulario) -> Investidor:
    document = formulario
    sheet = 'Assessor'
    df = pd.read_excel(document, sheet, skiprows=3, usecols=[2, 2])
    investidor = Investidor(df.values[11][0], df.values[23][0], df.values[8][0])
    return investidor


def read_files(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def build_config(investidor: Investidor) -> ChatConfig:
    return ChatConfig(
        model='genma12customFinance',
        messages=build_message(investidor)
    )


def print_output(chunk: str):
    txt = open('output.txt', 'w', encoding='utf-8')
    txt.write(chunk)


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
        f"""
You are a senior financial advisor tasked with creating a personalized investment portfolio. Your response must be concise, data-driven, and follow the requested format exactly.

## Contextual Information

### 1. Economic Indicators
* SELIC Rate: 15%
* IPCA (Inflation): 4.8%
* CDI Rate: 14.9%

### 2. Risk Profile Definitions & Asset's Definition
{rule}
    Profile: Super conservador
        Allocation: 100% pós fixados;
    
    Profile: Conservador
        Allocation: 65% pós fixado, 3% pré fixado, 20% IPCA, 12% multimercado;

    Profile: Moderado
        Allocation: 50% pós fixado, 3% pré fixado, 25% IPCA, 10% multimercado, 12% renda variavel;
    
    Profile: Arrojado
        Allocation: 40% pós fixado, 7% pré fixado, 23% IPCA, 7% multimercado, 23% renda variavel;
    
    Profile: Agressivo
        Allocation: 35% pós fixado, 3% pré fixado, 20% IPCA, 10% multimercado, 32% renda variavel;

### 3. Available Investment Products
{opportunity}

## Investor Data
* Risk Profile: {investidor.perfil}
* Net Worth: {investidor.patrimonioLiquido}
* Total Monthly Expenses: {investidor.despesasTotais}

## Your Task

1.  **State the Investor's Profile:** Begin by clearly stating the investor's risk profile.

2.  **Calculate Emergency Reserve:** Calculate the emergency reserve value, which must be exactly 10 times the total monthly expenses. Allocate this amount to the most suitable low-risk, high-liquidity asset from the "Available Investment Products".

3.  **Allocate Remaining Capital:** Subtract the emergency reserve from the total net worth. Allocate the remaining capital according to the asset allocation percentages defined in the "Risk Profile Definitions" for the investor's specific profile.

4.  **Construct and Present the Portfolio:** Display the final portfolio. Follow these strict rules:
    * Do not include any introductory or concluding comments, observations, or explanations.
    * For each investment class (e.g., Pós fixado, IPCA), select no more than four assets from the "Available Investment Products".
    * Present the final portfolio with the exact value in Reais (R$) for each class and each individual asset.
    * **All calculated monetary values in the final portfolio must be rounded to two decimal places.**
""")

    return [ChatMessage(role="user", content=mensagem)]


def use_ollama(config: ChatConfig) -> str:
    try:
        response = ollama.chat(
            model='genma12customFinance',
            messages=[message.__dict__ for message in config.messages],
            stream=config.stream,
            keep_alive=-1,
            options={"think": config.think}
        )
    except Exception as error:
        print(error)

    return response


def start(formulario):


    investidor = set_investors(formulario)
    config = build_config(investidor)
    config.stream = False
    print('loading task 1')
    response = use_ollama(config)

    # for chunk in response:
    #     print(chunk['message']['content'], end='', flush=True)


    return format_output(response.message.content).text
