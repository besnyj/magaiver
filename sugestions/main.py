from config import ChatConfig, ChatMessage
from investidor import Investidor
import ollama  # type: ignore
from typing import get_args
import os

def list_files(folder_name: str):
    return [file for file in os.listdir(folder_name) if file.endswith('.txt')]

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

    while True:
        try:
            rules = list_files(os.path.join(base_path, "rules"))
            print("\nrule list:")
            for index, rule in enumerate(rules, 1):
                 print(f"{index}. {rule}")
            rule = read_files(os.path.join(base_path, "rules", rules[int(input("Choose a rule: ")) - 1]))
            break
        except (ValueError, IndexError):
            print("Invalid selection \n")

    while True:
        try:
            profiles = list_files(os.path.join(base_path, "profiles"))
            print("\nprofile list:")
            for index, profile in enumerate(profiles, 1):
                print(f"{index}. {profile}")
            profile = read_files(os.path.join(base_path, "profiles", profiles[int(input("Choose a profile: ")) - 1]))
            break
        except (ValueError, IndexError):
            print("Invalid selection \n")
            
    while True:
        try:
            opportunities = list_files(os.path.join(base_path, "opportunities"))
            print("\nopportunity list:")
            for index, opportunity in enumerate(opportunities, 1):
                print(f"{index}. {opportunity}")
            opportunity = read_files(os.path.join(base_path, "opportunities", opportunities[int(input("Choose a opportunity: ")) - 1]))
            break
        except (ValueError, IndexError):
            print("Invalid selection \n")

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
    investidor = Investidor(100000.0, 3000.0, "moderado")

    config = build_config(investidor)
    response = use_ollama(config)
    
    for chunk in response:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    main()