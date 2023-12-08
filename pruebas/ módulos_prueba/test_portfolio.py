# pruebas/módulos_prueba/test_portfolio.py

import pytest
from crypto_tracker.módulos.cartera import Cartera
from crypto_tracker.módulos.moneda import Moneda

def test_cartera_agregar_moneda():
    cartera = Cartera()
    bitcoin = Moneda("Bitcoin", "BTC", 45000)
    ethereum = Moneda("Ethereum", "ETH", 3000)
    
    # Caso de prueba 1: Agregar una moneda a la cartera vacía
    cartera.agregar_moneda(bitcoin)
    assert bitcoin in cartera.monedas
    
    # Caso de prueba 2: Intentar agregar la misma moneda nuevamente
    cartera.agregar_moneda(bitcoin)
    assert len(cartera.monedas) == 1

    # Caso de prueba 3: Agregar otra moneda diferente
    cartera.agregar_moneda(ethereum)
    assert ethereum in cartera.monedas
    assert len(cartera.monedas) == 2

def test_cartera_eliminar_moneda():
    cartera = Cartera()
    bitcoin = Moneda("Bitcoin", "BTC", 45000)
    ethereum = Moneda("Ethereum", "ETH", 3000)
    
    cartera.agregar_moneda(bitcoin)
    cartera.agregar_moneda(ethereum)
    
    # Caso de prueba 1: Eliminar una moneda presente en la cartera
    cartera.eliminar_moneda(bitcoin)
    assert bitcoin not in cartera.monedas
    
    # Caso de prueba 2: Intentar eliminar una moneda que no está en la cartera
    with pytest.raises(ValueError, match="Bitcoin no está en tu cartera. No se eliminará."):
        cartera.eliminar_moneda(bitcoin)

def test_cartera_valor_total():
    cartera = Cartera()
    bitcoin = Moneda("Bitcoin", "BTC", 45000)
    ethereum = Moneda("Ethereum", "ETH", 3000)
    
    cartera.agregar_moneda(bitcoin)
    cartera.agregar_moneda(ethereum)
    
    # Caso de prueba 1: Verificar el valor total de la cartera
    assert cartera.valor_total() == 48000

    # Caso de prueba 2: Agregar otra moneda y verificar el nuevo valor total
    ripple = Moneda("Ripple", "XRP", 1.25)
    cartera.agregar_moneda(ripple)
    assert cartera.valor_total() == 48001.25
