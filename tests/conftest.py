# tests/conftest.py  ← just these 3 lines
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))