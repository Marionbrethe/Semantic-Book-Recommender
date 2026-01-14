import os
import pandas as pd

DEFAULT_RATED_BOOKS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),  # project root
    "data",
    "my_rated_books.csv",
)

def load_my_rated_books(path: str = DEFAULT_RATED_BOOKS_PATH) -> pd.DataFrame:
    """
    Load the user's rated books from CSV.
    Expected columns: title, author, rating, (optional) notes.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Rated books file not found at {path}")
    
    df = pd.read_csv(path)
    
    # Basic sanity checks
    required_cols = {"title", "author", "rating"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in {path}: {missing}")
    
    # Ensure rating is numeric
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df = df.dropna(subset=["rating"])
    
    return df

if __name__ == "__main__":
    # Quick manual test: run `python -m src.taste_vector` from project root
    books = load_my_rated_books()
    print(books)