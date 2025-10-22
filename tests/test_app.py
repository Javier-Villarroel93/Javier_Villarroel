# tests/test_app.py
import pytest
from src.app import suma

def test_suma_positivos():
    assert suma(2, 3) == 5

def test_suma_negativos():
    assert suma(-1, -2) == -3
