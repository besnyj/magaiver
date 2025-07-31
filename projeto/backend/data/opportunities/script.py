import json
import random
import locale

# Set the locale to Brazilian Portuguese for correct currency formatting.
# On some systems, you might need to install the locale:
# Linux: sudo locale-gen pt_BR.UTF-8
# Windows/macOS: 'pt_BR.UTF-8' or 'Portuguese_Brazil.1252' might work.
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    print("Warning: 'pt_BR.UTF-8' locale not found. Using default. Currency formatting might be incorrect.")

# --- Data from our previous conversations ---

PROFILES = {
    "Super conservative": {
        "Pós-Fixado": 1.00
    },
    "Conservative": {
        "Pós-Fixado": 0.65,
        "Pré-Fixado": 0.03,
        "IPCA": 0.20,
        "Fundos Multimercado": 0.12
    },
    "Moderate": {
        "Pós-Fixado": 0.50,
        "Pré-Fixado": 0.03,
        "IPCA": 0.25,
        "Fundos Multimercado": 0.10,
        "Renda Variável": 0.12
    },
    "Semi-Agressive": {
        "Pós-Fixado": 0.40,
        "Pré-Fixado": 0.07,
        "IPCA": 0.23,
        "Fundos Multimercado": 0.07,
        "Renda Variável": 0.23
    },
    "Agressive": {
        "Pós-Fixado": 0.35,
        "Pré-Fixado": 0.03,
        "IPCA": 0.20,
        "Fundos Multimercado": 0.10,
        "Renda Variável": 0.32
    }
}

ASSETS = {
    "Reserva de emergencia": [
        "CDB Banco Volkswagen (2026/100% CDI)",
        "CDB Banco Carrefour (2026/100% CDI)"
    ],
    "Pós-Fixado": [
        "LCA BTG Pactual (2026/90%CDI)", "LCI BRB (2026/92% CDI)", "LCA Original (2026/94% CDI)",
        "LCA Banco Rodobens (2027/88,6%)", "LCA BTG Pactual (2027/90% CDI)", "LCA Banco Inter (2027/90% CDI)",
        "CDB Luso Brasileiro (2027/107% CDI)", "CDB BS2 (2027/106% CDI)", "CDB Original (2028/107% CDI)",
        "CDB Fator (2028/108% CDI)", "CDB BDMG (2029/107% CDI)", "CDB Digimais (2029/110% CDI)",
        "CDB BDMG (2030/108% CDI)", "CDB Banco Digimais (2030/112% CDI)", "CDB NBC Bank (2031/106% CDI)",
        "CDB NBC Bank (2032/106% CDI)", "CDB BS2 (2027/CDI + 0,75%)", "CDB Original (2028/CDI + 0,92%)",
        "CDB Andbank (2028/CDI +0,85%)", "CRI JHSF (2029/100% CDI)", "CRA Minerva (2029/99% CDI)",
        "CRI Iguatemi (2030/97% CDI)", "CRA Vamos (2030/CDI + 1,30%)", "CRA CMAA (2034/CDI + 1,35%)"
    ],
    "Pré-Fixado": [
        "CDB Picpay (2027/14,45%)", "CDB Banco C6 (2027/14,35%)", "CDB NBC Bank (2027/14,27%)",
        "CDB Banco XP (2027/14,40%)", "CDB Banco BBC (2028/14,45%)", "CDB Andbank (2028/14,30%)",
        "CDB NBC Bank (2032/14,66%)", "CRI Soma (2029/13,45%)", "CRA Zamp (2029/14,20%)",
        "CRA BRF (2031/13,20%)", "CRA Marfrig (2031/13,20%)", "CRA Minerva (2032/14,10%)"
    ],
    "IPCA": [
        "CDB Banco XP (2027/IPCA + 9,05%)", "CDB Agibank (2028/IPCA + 7,85%)", "CDB BS2 (2028/IPCA + 7,85%)",
        "CDB Daycoval (2029/IPCA + 7,50%)", "CDB Banco XP (2029/IPCA + 7,75%)", "CDB Banco XP (2030/IPCA + 7,70%)",
        "CDB Daycoval (2030/IPCA + 7,37%)", "CDB Fibra (2030/IPCA + 7,95%)", "CDB Fibra (2031/IPCA + 7,90%)",
        "CDB BMG (2032/IPCA + 7,25%)", "CRI MRV (2029/IPCA + 9,15%)", "CRI Rede D’Or (2029/IPCA + 7,75%)",
        "CRA Vamos (2030/IPCA + 8,85%)", "CRA BRF (2032/IPCA + 7,90%)", "CRA Marfrig (2032/IPCA + 7,90%)",
        "CRA BTG (2033/IPCA + 7,20%)", "CRA CMAA (2034/IPCA + 8,75%)"
    ],
    "Fundos Multimercado": [
        "Genoa Capital Radar FIC FIM", "Giant Zarathustra FIC FIM", "Ibiuna Hedge STH FIC FIM",
        "JGP Strategy FIC FIM", "Kinea Chronos FIM", "Legacy Capital FIC FIM",
        "SPX Nimitz Gripen Advisory FIC FIM", "Verde AM X60 Advisory FIC FIM"
    ],
    "Renda Variável": [
        "Alupart (ALUP11)", "B3 (B3SA3)", "Banco do Brasil (BBAS3)", "Cemig (CMIG4)",
        "Copel (CPLE6)", "Eletrobras (ELET3)", "Itau Unibanco (ITUB4)", "Petrobras (PETR4)",
        "TIM (TIMS3)", "Vale (VALE3)", "Vivo (VIVT3)"
    ]
}


def format_currency(value):
    """Formats a float into a BRL currency string."""
    return locale.currency(value, symbol=True, grouping=True)


def generate_portfolio():
    """Generates a single, random portfolio example."""

    # 1. Generate random scenario data
    profile_name = random.choice(list(PROFILES.keys()))
    net_worth = random.uniform(50000, 5000000)
    # Ensure expenses are realistic relative to net worth
    max_expense = net_worth / 24  # Arbitrary ratio to keep it sensible
    monthly_expenses = random.uniform(2000, max(2001, max_expense))

    # 2. Construct the instruction string
    instruction = (
        "Given the following rules and investor data, create a detailed investment portfolio. "
        "Rules: 1. State the investor's profile. "
        "2. Calculate an emergency reserve equal to 10x the total monthly expenses and allocate it to assets from the 'Reserva de emergencia' category. "
        "3. Allocate the remaining capital according to the asset allocation percentages for the investor's specific profile. "
        "4. Construct the portfolio by selecting no more than four assets for each investment class from the provided 'Available Investment Products' list. "
        "5. Present the final portfolio using the exact format provided, with no introductory or concluding text. "
        f"--- Investor Data: Profile: {profile_name}; Net Worth: {format_currency(net_worth)}; Total Monthly Expenses: {format_currency(monthly_expenses)}."
    )

    # 3. Perform calculations
    emergency_reserve_total = 10 * monthly_expenses
    remaining_capital = net_worth - emergency_reserve_total

    if remaining_capital < 0:
        return None  # Skip this iteration if expenses are too high for the net worth

    allocations = PROFILES[profile_name]

    # 4. Construct the output string
    output_parts = [f"Perfil do Investidor: {profile_name}\n"]

    # --- Emergency Reserve ---
    output_parts.append("Reserva de Emergência")
    output_parts.append(f"* Valor Total da Classe: {format_currency(emergency_reserve_total)}")

    # Allocate emergency funds (1 or 2 assets)
    num_er_assets = random.randint(1, 2)
    selected_er_assets = random.sample(ASSETS["Reserva de emergencia"], num_er_assets)
    er_allocs = [emergency_reserve_total / num_er_assets] * num_er_assets
    for i, asset in enumerate(selected_er_assets):
        output_parts.append(f"* {asset}: {format_currency(er_allocs[i])}")

    # --- Other Asset Classes ---
    class_map = {
        "Pós-Fixado": "Pós-Fixado",
        "Pré-Fixado": "Pré-Fixado",
        "IPCA": "IPCA",
        "Fundos Multimercado": "Fundos Multimercado",
        "Renda Variável": "Renda Variável"
    }

    for class_name, percentage in allocations.items():
        class_total = remaining_capital * percentage
        if class_total <= 0:
            continue

        output_parts.append(f"\n{class_map[class_name]}")
        output_parts.append(f"* Valor Total da Classe: {format_currency(class_total)}")

        # Select assets for the class (1 to 4)
        available_assets = ASSETS[class_map[class_name]]
        max_assets_in_class = min(len(available_assets), 4)
        num_assets = random.randint(1, max_assets_in_class)
        selected_assets = random.sample(available_assets, num_assets)

        # Distribute value among selected assets
        asset_allocs = [class_total / num_assets] * num_assets
        for i, asset in enumerate(selected_assets):
            output_parts.append(f"* {asset}: {format_currency(asset_allocs[i])}")

    return {"instruction": instruction, "output": "\n".join(output_parts)}


# --- Main execution ---
if __name__ == "__main__":
    dataset = []
    while len(dataset) < 1000:
        portfolio = generate_portfolio()
        if portfolio:  # Add to dataset only if valid
            dataset.append(portfolio)
            if len(dataset) % 100 == 0:
                print(f"Generated {len(dataset)}/1000 examples...")

    # Write to a .jsonl file
    file_path = "investment_portfolios.jsonl"
    with open(file_path, 'w', encoding='utf-8') as f:
        for entry in dataset:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

    print(f"\nSuccessfully generated 1000 examples in '{file_path}'")

    # Print the first 2 examples as a preview
    print("\n--- PREVIEW OF THE FIRST 2 EXAMPLES ---")
    for i in range(2):
        print(f"\n--- EXAMPLE {i + 1} ---")
        print("INSTRUCTION:")
        print(dataset[i]["instruction"])
        print("\nOUTPUT:")
        print(dataset[i]["output"])