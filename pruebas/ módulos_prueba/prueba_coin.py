# pruebas/módulos_prueba/prueba_coin.py

import pytest
from crypto_tracker.módulos.moneda import Moneda

def test_moneda_obtener_informacion():
    bitcoin = Moneda("Bitcoin", "BTC", 45000)
    assert bitcoin.obtener_informacion() == "Bitcoin (BTC): $45,000.00"

def test_moneda_actualizar_precio():
    ethereum = Moneda("Ethereum", "ETH", 3000)

    # Caso de prueba 1: Actualizar el precio con un valor positivo
    ethereum.actualizar_precio(3500)
    assert ethereum.precio == 3500

    # Caso de prueba 2: Intentar actualizar el precio con un valor negativo
    with pytest.raises(ValueError, match="El precio no puede ser negativo. No se actualizará."):
        ethereum.actualizar_precio(-500)

def test_moneda_str():
    ripple = Moneda("Ripple", "XRP", 1.25)
    assert str(ripple) == "Ripple (XRP): $1.25"

def test_moneda_igualdad():
    litecoin1 = Moneda("Litecoin", "LTC", 150)
    litecoin2 = Moneda("Litecoin", "LTC", 150)
    assert litecoin1 == litecoin2

    bitcoin = Moneda("Bitcoin", "BTC", 45000)
    assert litecoin1 != bitcoin
