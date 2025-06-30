class Investidor:
    def __init__(self, patrimonio_liquido: float, despesas_totais: float, perfil: str):
        self.patrimonioLiquido = patrimonio_liquido
        self.despesasTotais = despesas_totais
        self.perfil = perfil

    def __str__(self):
        return (f"Perfil: {self.perfil}\n"
                f"Patrimônio Líquido: R${self.patrimonioLiquido:,.2f}\n"
                f"Despesas Totais Mensais: R${self.despesasTotais:,.2f}")
