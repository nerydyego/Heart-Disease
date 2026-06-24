# Heart-Disease

Projeto de análise de registros clínicos de pacientes cardíacos com foco em classificação binária (presença/ausência de doença cardíaca). Este repositório contém utilitários para baixar e carregar o dataset, notebooks de análise e material de apoio.

Links

- Dataset: https://www.kaggle.com/datasets/yasserh/heart-disease-dataset?select=heart.csv
- Repositório: https://github.com/nerydyego/Heart-Disease

Resumo rápido

- Utilitários: `src/data_loader.py` — funções `baixar_dataset_kaggle()` e `carregar_csv()`.
- Notebook inicial: `notebook/analise.ipynb` — EDA, limpeza básica e estatísticas descritivas.
- Estrutura pronta para desenvolvimento com `pyproject.toml` / `requirement.txt`.

Instalação

```bash
python -m pip install --upgrade pip
pip install -e .
pip install -r requirement.txt
```

Configurar acesso ao Kaggle

1. Crie uma conta no Kaggle e gere `kaggle.json` (API token).
2. Coloque `kaggle.json` na pasta adequada (ex.: `~/.kaggle/`) ou exponha via variáveis de ambiente.
3. Não comite esse arquivo no repositório.

Uso (exemplo)

```python
from src.data_loader import baixar_dataset_kaggle, carregar_csv

baixar_dataset_kaggle('yasserh/heart-disease-dataset', destino='data/raw', unzip=True)
df = carregar_csv('data/raw/heart.csv')
print(df.head())
```

Resumo das ações no notebook

- Download e extração do dataset em `data/raw`.
- Carregamento dos dados e inspeção inicial (`head()`, `info()`, `shape`).
- Renomeação das colunas para rótulos em português.
- Remoção de duplicados e análise descritiva (contagens, percentuais, estatísticas).

Estrutura do repositório

- `src/` — código fonte.
- `notebook/` — notebooks de análise.
- `data/` — dados locais (ignorados por `.gitignore`).
- `hipoteses/`, `image/` — documentos e imagens locais (atualmente ignorados por `.gitignore`).

Notas sobre `.gitignore`

- O arquivo `.gitignore` exclui ambientes virtuais, caches, artefatos de build, dados e pastas locais como `hipoteses/` e `image/`.
- Se pretende versionar `hipoteses/` ou `image/`, remova essas entradas do `.gitignore` antes de commitar.
``

Próximos passos recomendados

- Completar o notebook com EDA avançada e modelos de classificação.
- Adicionar testes unitários para os utilitários (ex.: `tests/test_data_loader.py`).
- Configurar CI (GitHub Actions) para rodar testes e lint automaticamente.

Contribuição

Abra uma issue ou pull request: https://github.com/nerydyego/Heart-Disease
