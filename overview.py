import pandas as pd


class Integracacao:

    @staticmethod
    def GetDocument():
        documentAddress = "C:/Users/Felipe/Downloads/Overview.xlsx"
        sheet = 'Assessor'

        df = pd.read_excel(documentAddress, sheet, skiprows=3, usecols=[2,2])

        return df

    def GetRiskProfile(self):
        return self.values[8]

    def GetPL(self):
        return self.values[11]

    def GetExpenses(self):
        return self.values[23]

class Investidor:

    patrimonioLiquido = Integracacao.GetPL(Integracacao.GetDocument())[0]
    perfil = str(Integracacao.GetRiskProfile(Integracacao.GetDocument())[0])
    despesasTotais = Integracacao.GetExpenses(Integracacao.GetDocument())[0]

