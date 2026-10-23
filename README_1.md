# Consolidador de planilhas de vendas

Script em Python que lê várias planilhas mensais de vendas, junta tudo em uma
única tabela e gera um relatório em Excel com os totais por vendedor, por loja
e por mês.

> Todos os dados deste projeto são fictícios e gerados por `gerar_dados.py`.

## O problema que resolve
Juntar planilhas de vários meses na mão é lento e dá erro. Este script faz isso
em segundos e **avisa quando uma planilha está fora do padrão**, em vez de
gerar um relatório com números errados.

## O que ele faz
- Lê todos os arquivos `vendas_*.xlsx` de uma pasta
- Padroniza os nomes das colunas (`Valor`, `VALOR` e ` valor ` viram `valor`)
- Para com uma mensagem clara se faltar alguma coluna, dizendo qual arquivo e qual coluna
- Calcula o total de cada venda e soma por vendedor, loja e mês
- Salva um `relatorio.xlsx` com 4 abas

## Como usar
```bash
pip install -r requirements.txt
python gerar_dados.py        # cria planilhas de exemplo na pasta "vendas"
python consolidar.py         # gera o relatorio.xlsx
```

Para usar outra pasta ou outro nome de saída:
```bash
python consolidar.py --pasta minhas_planilhas --saida resultado.xlsx
```

## Tecnologias
Python, pandas, openpyxl.

## Possíveis melhorias
- Enviar o relatório por e-mail automaticamente
- Gráficos no Excel
- Aceitar arquivos CSV
