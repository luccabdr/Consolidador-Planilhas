from pathlib import Path
import pandas as pd

pasta = Path("vendas")
tabelas = []

for arquivo in sorted(pasta.glob("vendas_*.xlsx")):
    df = pd.read_excel(arquivo)
    df["mes"] = arquivo.stem.replace("vendas_", "")
    tabelas.append(df)

vendas = pd.concat(tabelas, ignore_index=True)
vendas["total"] = vendas["quantidade"] * vendas["valor"]

def total_por(coluna):
    return vendas.groupby(coluna)["total"].sum().round(2).sort_values(ascending=False)

por_vendedor = total_por("vendedor")
por_loja = total_por("loja")
por_mes = total_por("mes")

print(por_vendedor, por_loja, por_mes, sep="\n\n")

with pd.ExcelWriter("relatorio.xlsx") as saida:
    vendas.to_excel(saida, sheet_name="todas_as_vendas", index=False)
    por_vendedor.to_excel(saida, sheet_name="por_vendedor")
    por_loja.to_excel(saida, sheet_name="por_loja")
    por_mes.to_excel(saida, sheet_name="por_mes")

print("relatorio.xlsx criado!")