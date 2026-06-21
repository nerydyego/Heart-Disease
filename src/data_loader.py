from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

def baixar_dataset_kaggle(
    dataset: str,
    destino: str = "data",
    unzip: bool = True
) -> Path:
    """
    Baixa um dataset do Kaggle e salva dentro do projeto.

    Parameters
    ----------
    dataset : str
        Identificador do dataset no Kaggle.
        Exemplo: 'yasserh/heart-disease-dataset'

    destino : str
        Pasta onde os arquivos serão salvos.
        Padrão: 'data/raw'

    unzip : bool
        Se True, descompacta automaticamente o arquivo baixado.

    Returns
    -------
    Path
        Caminho da pasta onde o dataset foi salvo.
    """

    destino_path = Path(destino)
    destino_path.mkdir(parents=True, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        dataset=dataset,
        path=destino_path,
        unzip=unzip
    )

    return destino_path

def carregar_csv(caminho: str) -> pd.DataFrame:
    """
    Carrega um arquivo CSV para um `pandas.DataFrame`.

    Parameters
    ----------
    caminho : str
        Caminho para o arquivo CSV. Pode ser `str` ou `Path`.

    Returns
    -------
    pd.DataFrame
        DataFrame contendo os dados carregados do CSV.

    Raises
    ------
    FileNotFoundError
        Se o arquivo especificado não existir.
    pandas.errors.EmptyDataError
        Se o arquivo estiver vazio.
    """

    caminho_path = Path(caminho)
    if not caminho_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    return pd.read_csv(caminho_path)