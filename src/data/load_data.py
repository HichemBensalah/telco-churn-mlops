import os
import pandas as pd


def get_project_root() -> str:
    """
    Retourne le chemin absolu de la racine du projet.
    (le dossier qui contient 'data', 'src', etc.)
    """
    # __file__ = src/data/load_data.py
    # os.path.dirname(__file__)        -> .../src/data
    # os.path.dirname(..)              -> .../src
    # os.path.dirname(..)              -> .../ (racine projet)
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load_raw_telco_data(filename: str = "telco_churn.csv") -> pd.DataFrame:
    """
    Charge le fichier brut Telco Churn depuis data/raw.
    """

    root_dir = get_project_root()
    data_path = os.path.join(root_dir, "data", "raw", filename)

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Fichier introuvable : {data_path}")

    df = pd.read_csv(data_path)
    return df


if __name__ == "__main__":
    df = load_raw_telco_data()
    print(df.head())
    print(f"\nShape du dataset : {df.shape}")
