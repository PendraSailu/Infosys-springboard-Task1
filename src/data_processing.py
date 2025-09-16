import pandas as pd
from typing import IO

def load_data(file: IO) -> pd.DataFrame:
    """
    Load a CSV or JSON file-like object into a pandas DataFrame.
    Works with Streamlit UploadedFile.
    """
    # try to infer from filename
    name = getattr(file, "name", "").lower()
    try:
        if name.endswith(".csv"):
            return pd.read_csv(file)
        if name.endswith(".json"):
            return pd.read_json(file)
    except Exception:
        # reset pointer and try flexible parsing
        try:
            file.seek(0)
        except Exception:
            pass

    # fallback: try CSV then JSON
    try:
        return pd.read_csv(file)
    except Exception:
        try:
            file.seek(0)
        except Exception:
            pass
        return pd.read_json(file)
