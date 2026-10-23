import random
from pathlib import Path
import pandas as pd

pasta = Path("vendas")
pasta.mkdir(exist_ok=True)

vendedores = ["Ana", "Bruno", "Carla", "Diego"]
produtos = ["Camiseta", "Calça", "Tênis", "Boné"]
lojas = ["Loja 1", "Loja 2", "Loja 3", "Loja 4"]

for mes in ["janeiro", "fevereiro", "marco"]:
    linhas = []
    for _ in range(20):
        linhas.append({
            "loja": random.choice(lojas),
            "vendedor": random.choice(vendedores),
            "produto": random.choice(produtos),
            "quantidade": random.randint(1, 5),
            "valor": round(random.uniform(30, 300), 2),
        })
    pd.DataFrame(linhas).to_excel(pasta / f"vendas_{mes}.xlsx", index=False)

print("Planilhas criadas!")