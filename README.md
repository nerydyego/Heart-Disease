# Heart-Disease

Projeto de análise de registros clínicos de pacientes cardíacos com foco em classificação binária (presença/ausência de doença cardíaca).

Visão geral
- Objetivo: explorar, limpar e modelar o dataset "Heart Disease Dataset" (Kaggle) para pesquisa e ensino.
- Dataset: [heart.csv (Kaggle)](https://www.kaggle.com/datasets/yasserh/heart-disease-dataset?select=heart.csv)
- Repositório: https://github.com/nerydyego/Heart-Disease

Instalação rápida

```bash
pip install -e .
```

Pré-requisitos
- Python 3.8+ e `pip`.
- Credenciais do Kaggle configuradas localmente (arquivo `kaggle.json` ou variáveis de ambiente).

Uso (exemplo)

```python
from src.data_loader import baixar_dataset_kaggle, carregar_csv

baixar_dataset_kaggle('yasserh/heart-disease-dataset', destino='data', unzip=True)
df = carregar_csv('data/heart.csv')
print(df.head())
```

Estrutura e observações sobre versionamento

- `src/` - código fonte e utilitários (ex.: [src/data_loader.py](src/data_loader.py#L1-L200)).
- `notebook/` - notebooks de análise (ex.: `notebook/analise.ipynb`).
- `data/` - pasta local para dados baixados (não comitada).
- `hipoteses/` e `image/` - pastas locais com hipóteses, dicionários e imagens; atualmente **ignoradas** pelo Git via `.gitignore` (ou seja, não são enviadas ao repositório remoto). Se quiser versioná-las, remova as entradas correspondentes em `.gitignore`.

Pontos importantes
- Não comitar credenciais nem tokens (ex.: `kaggle.json`, `Token_kaggle.txt`). Use variáveis de ambiente ou um gerenciador de segredos.
- Grandes arquivos de dados devem permanecer fora do repositório; use `data/` local ou armazenamento externo.

 Resumo das alterações em `notebook/analise.ipynb`
 
 - Script inicial de importação: uso de `baixar_dataset_kaggle()` para baixar e descompactar o dataset em `data/raw`.
 - Carregamento dos dados com `carregar_csv()` e inspeção inicial (`head()`, `info()`, `shape`).
 - Renomeação das colunas para versões em português (ex.: `Idade`, `Sexo`, `dor_toracica`, `Cardiaco`).
 - Remoção de duplicados com `drop_duplicates()`.
 - Cálculo de contagens e percentuais da variável alvo (`Cardiaco`) e distribuição por sexo.
 - Estatística descritiva de colunas numéricas (idade, PA em repouso, colesterol, FC máxima, ST depressão).
 - Comentários iniciais indicando distribuição aproximadamente equilibrada entre casos positivos e negativos.
 
 Próximos passos recomendados
 - Finalizar o notebook com EDA, limpeza, engenharia de features e pipeline de treino.
 - Implementar testes unitários (por exemplo, teste para `carregar_csv()` em `tests/test_data_loader.py`).
 - Adicionar integração contínua (GitHub Actions) para rodar testes e lint automaticamente.
 
 Contato / Contribuição
 - Para contribuições, abra uma issue ou pull request: https://github.com/nerydyego/Heart-Disease
 
 Licença
 - Adicione um arquivo `LICENSE` ao repositório (ex.: MIT) antes de torná-lo público.

Próximos passos sugeridos
- Finalizar o notebook com EDA, limpeza e modelagem.
- Adicionar testes unitários para utilitários em `src/`.
- Configurar CI para testes e lint.

Contribuição
- Abra issues ou pull requests no GitHub: https://github.com/nerydyego/Heart-Disease


Licença

- Adicione um arquivo `LICENSE` apropriado (ex.: MIT).

