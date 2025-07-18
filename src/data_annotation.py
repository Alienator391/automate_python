import requests
import pandas as pd

def draw_doc_grid(doc_url: str) -> None:
    """Fetch a published-web Google Doc and print its character grid."""
    # 1) Download HTML
    html = requests.get(doc_url).text          # Google Docs is UTF-8
    
    # 2) Grab the first HTML <table> as a DataFrame
    df = pd.read_html(html, header=0)[0]                   # → columns: x-coordinate, Character, y-coordinate
    print(df.head())
    # 3) Build a dict keyed by (x, y)
    grid = {(int(row['x-coordinate']), int(row['y-coordinate'])): str(row['Character'])
            for _, row in df.iterrows()}
    
    # 4) Determine bounds
    max_x = max(x for x, _ in grid.keys())
    max_y = max(y for _, y in grid.keys())
    
    # 5) Print the grid
    for y in range(max_y + 1):
        line = ''.join(grid.get((x, y), ' ') for x in range(max_x + 1))
        print(line)

if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vSZ1vDD85PCR1d5QC2XwbXClC1Kuh3a4u0y3VbTvTFQI53erafhUkGot24ulET8ZRqFSzYoi3pLTGwM/pub"
    draw_doc_grid(url)