from pathlib import Path
from src.regex_search import get_file_names

def test_get_file_names_returns_txt_only(tmp_path: Path):
     (tmp_path / "a.txt").write_text("hi")
     (tmp_path / "b.txt").write_text("bye")
     (tmp_path / "image.png").write_text("not txt")

     result = get_file_names(tmp_path)
     # Assert   (check the outcome)
     assert sorted(result) == ["a.txt", "b.txt"]