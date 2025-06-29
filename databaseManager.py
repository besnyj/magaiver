import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


def addAlocaveis():

    risco = int(input("risco: "))
    emissor = input("emissor: ")
    tipo = input("tipo: ")
    vencimento = int(input("ano do vencimento: "))
    rendimento = input("rendimento: ")

    cursor.execute(f"""INSERT INTO alocaveis VALUES ({risco}, '{emissor}',
        '{tipo}', {vencimento}, '{rendimento}')""")
    connection.commit()

def addRules():

    numberRules = cursor.execute("""SELECT * FROM rules""").fetchall()

    rule = input("rule: ")
    cursor.execute(f"""INSERT INTO rules VALUES ({len(numberRules)+1}, '{rule}')""")

    connection.commit()

while True:
    addRules()