# crypto_tracker/principal.py

from módulos.moneda import Moneda
from módulos.cartera import Cartera

def iniciar_aplicacion():
    print("¡Bienvenido a CryptoTracker!")

    # Crear una cartera e iniciar con algunas criptomonedas
    mi_cartera = Cartera()
    inicializar_cartera(mi_cartera)

    # Mostrar el estado inicial de la cartera
    mostrar_estado_cartera(mi_cartera)

    # Interacción del usuario
    while True:
        opcion = obtener_opcion_usuario()

        if opcion == 1:
            agregar_moneda(mi_cartera)
        elif opcion == 2:
            mostrar_estado_cartera(mi_cartera)
        elif opcion == 3:
            print("¡Gracias por usar CryptoTracker! Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

def inicializar_cartera(cartera):
    # Iniciar la cartera con algunas criptomonedas
    bitcoin = Moneda("Bitcoin", "BTC", 45000)
    ethereum = Moneda("Ethereum", "ETH", 3000)

    cartera.agregar_moneda(bitcoin)
    cartera.agregar_moneda(ethereum)

def mostrar_estado_cartera(cartera):
    print("\nEstado Actual de la Cartera:")
    
    if not cartera.monedas:
        print("Tu cartera está vacía.")
    else:
        for moneda in cartera.monedas:
            print(moneda.obtener_información())

        print("\nValor Total de la Cartera: $", cartera.valor_total())

def obtener_opcion_usuario():
    print("\nOpciones:")
    print("1. Agregar Criptomoneda")
    print("2. Mostrar Estado de la Cartera")
    print("3. Salir")

    while True:
        try:
            opcion = int(input("Elige una opción: "))
            return opcion
        except ValueError:
            print("Por favor, ingresa un número válido.")

def agregar_moneda(cartera):
    nombre = input("Ingresa el nombre de la criptomoneda: ")
    símbolo = input("Ingresa el símbolo de la criptomoneda: ")

    while True:
        try:
            precio = float(input("Ingresa el precio de la criptomoneda: $"))
            break
        except ValueError:
            print("Por favor, ingresa un número válido para el precio.")

    nueva_moneda = Moneda(nombre, símbolo, precio)
    cartera.agregar_moneda(nueva_moneda)
    print(f"{nombre} ha sido agregada a tu cartera.")

if __name__ == "__main__":
    iniciar_aplicacion()
