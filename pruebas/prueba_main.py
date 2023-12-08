# pruebas/prueba_main.py

import pytest
from crypto_tracker.módulos.utils import validar_numero_positivo, formatear_dinero

def test_validar_numero_positivo():
    assert validar_numero_positivo("10", "Test") == 10
    assert validar_numero_positivo("0.5", "Test") == 0.5
    with pytest.raises(ValueError, match="Test debe ser un número válido."):
        validar_numero_positivo("-5", "Test")
    with pytest.raises(ValueError, match="Test debe ser un número válido."):
        validar_numero_positivo("texto", "Test")

def test_formatear_dinero():
    assert formatear_dinero(10) == "$10.00"
    assert formatear_dinero(1234.567) == "$1234.57"
    assert formatear_dinero(0.1) == "$0.10"
