import ollama
import classes
from overview import Investidor


#rules = classes.Databases.cursor.execute("""SELECT description FROM rules""").fetchall()

rules = open('rules.txt', encoding="utf8")
rules = rules.read()

def task():

    setRules = rules
    setProfiles = classes.Documentos.riskProfile


    task2 = (f'Use this information as your context: {setRules}; {setProfiles}; {classes.Documentos.oportunidades}; SELIC hoje é 15%. IPCA hoje é 4.8%. CDI hoje é 14.9%. Essas taxas podem parecer altas demais, mas são normais para o Brasil.\n'
             f'Sua tarefa: Crie um portifolio de investimentos de {Investidor.patrimonioLiquido} reais para um perfil {Investidor.perfil}'
             f'Separe parte do valor do portifolio para reserva de emergencia no valor de 10x{Investidor.despesasTotais}. A % da reserva de emergencia faz parte da % total para pos fixados.'
             f'Cada classe de investimento deve ter no máximo 4 ativos.'
             f'Liste o portifolio com os ativos escolhidos por classe e com os valores em cada ativo. Sem comentarios ou observacoes. ')
    response = ollama.chat(model=classes.Models.model1,
                               messages=[{
                                   'role':'user',
                                   'content': f'{task2}'
                               }], stream=False, think=False)
    
    response2 = ollama.chat(model=classes.Models.model1,
                            messages=[{
                                'role':'user',
                                'content': f'{response.message}; Round up the numbers to multiples of 1000s'
                            }], stream=True, think=False)
    
    for chunk in response2:
        print(chunk['message']['content'], end='', flush=True)


print("loading task")
task()
