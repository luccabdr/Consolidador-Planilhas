# Consolidador de Planilhas Excel

**Automatize a consolidação de vendas e a geração de relatórios utilizando Python.**

Projeto desenvolvido para reunir múltiplas planilhas Excel em uma única base de dados, calcular o faturamento e gerar relatórios organizados por vendedor, loja e mês.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## Sobre o projeto

O Consolidador de Planilhas Excel automatiza o processamento de dados comerciais, reduzindo o trabalho manual de reunir informações de diferentes arquivos.

O programa identifica arquivos de vendas, combina os registros, calcula o faturamento de cada venda e gera um relatório Excel com diferentes análises.

## Funcionalidades

- Leitura automática de múltiplos arquivos Excel.
- Consolidação dos dados em uma única tabela.
- Cálculo do faturamento por venda.
- Relatórios de faturamento por vendedor.
- Relatórios de faturamento por loja.
- Análise de faturamento por mês.
- Exportação dos resultados para um arquivo Excel com abas separadas.

## Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **Pandas:** manipulação, organização e análise dos dados.
- **Pathlib:** gerenciamento dos caminhos e arquivos.
- **OpenPyXL:** leitura e escrita de arquivos Excel.

## Estrutura do projeto

```text
Consolidador-Planilhas/
├── gerar_planilhas.py
├── consolidador.py
├── README.md
├── LICENÇA
└── vendas/
    ├── vendas_janeiro.xlsx
    ├── vendas_fevereiro.xlsx
    └── vendas_marco.xlsx
```

## Como executar

### 1. Pré-requisitos

Instale o [Python](https://www.python.org/downloads/) e as dependências:

```bash
python -m pip install pandas openpyxl
```

### 2. Gerar as planilhas de exemplo

```bash
python gerar_planilhas.py
```

Esse comando cria arquivos fictícios de vendas na pasta `vendas`.

### 3. Consolidar as vendas

```bash
python consolidador.py
```

Ao finalizar, o programa gera o arquivo `relatorio.xlsx` com os dados consolidados e os relatórios por vendedor, loja e mês.

## Exemplo de resultado

O relatório gerado contém as seguintes abas:

| Aba | Conteúdo |
|---|---|
| `todas_as_vendas` | Registros consolidados e faturamento por venda |
| `por_vendedor` | Faturamento total de cada vendedor |
| `por_loja` | Faturamento total de cada loja |
| `por_mes` | Faturamento total de cada mês |

## Objetivo

Este projeto faz parte do meu aprendizado em Python, automação de tarefas e análise de dados, com foco no desenvolvimento de soluções práticas para organizar informações e facilitar a geração de relatórios.

## Licença

Este projeto está licenciado sob a licença MIT.

---

Desenvolvido por **Lucca Belloni Del Rey**.
