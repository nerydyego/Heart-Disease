# Heart-Disease

Projeto de análise de registros clínicos de pacientes cardíacos com foco em classificação binária (presença/ausência de doença cardíaca).

Visão geral
- Objetivo: explorar, limpar e modelar o dataset "Heart Disease Dataset" (Kaggle) para pesquisa e aprendizagem.
- Dataset: [heart.csv (Kaggle)](https://www.kaggle.com/datasets/yasserh/heart-disease-dataset?select=heart.csv)
- Repositório: https://github.com/nerydyego/Heart-Disease

Começando (rápido)

1) Pré-requisitos

- Python 3.8+ instalado
- Credenciais do Kaggle configuradas (arquivo `kaggle.json` na pasta apropriada). Veja a documentação do Kaggle para mais detalhes.

2) Instalação (desenvolvimento)

```bash
pip install -e .
```

3) Exemplo de uso

```python
from src.data_loader import baixar_dataset_kaggle, carregar_csv

# Baixa e extrai o dataset do Kaggle
baixar_dataset_kaggle('yasserh/heart-disease-dataset', destino='data', unzip=True)

# Carrega o CSV principal
df = carregar_csv('data/heart.csv')
print(df.shape)
```

Onde olhar
- Código utilitário: [src/data_loader.py](src/data_loader.py#L1-L400) — contém `baixar_dataset_kaggle()` e `carregar_csv()`.
- Notebook de análise: [notebook/analise.ipynb](notebook/analise.ipynb)

Boas práticas
- Não comitar credenciais (`kaggle.json`) ou dados sensíveis.
- Manter grandes datasets fora do repositório; use `data/` local ou armazenamento externo.

Próximos passos sugeridos
- Finalizar o notebook com EDA, limpeza, engenharia de features e validação de modelos.
- Adicionar testes unitários (ex.: para `carregar_csv`).
- Criar CI básico para executar testes e lint.

Contribuição
- Abra issues ou pull requests no GitHub para discutir alterações.

Licença
- Adicione um arquivo `LICENSE` para especificar a licença do projeto (ex.: MIT).
