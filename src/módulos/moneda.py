# crypto_tracker/módulos/moneda.py

class Moneda:
    def __init__(self, nombre, símbolo, precio):
        self.nombre = nombre
        self.símbolo = símbolo
        self.precio = precio

    def obtener_informacion(self):
        return f"{self.nombre} ({self.símbolo}): ${self.precio:.2f}"

    def actualizar_precio(self, nuevo_precio):
        if self._validar_precio(nuevo_precio):
            self.precio = nuevo_precio
            print(f"¡El precio de {self.nombre} ha sido actualizado a ${self.precio:.2f}!")
        else:
            print("Error al actualizar el precio. Asegúrate de ingresar un valor no negativo.")

    def _validar_precio(self, nuevo_precio):
        return nuevo_precio >= 0

    def __str__(self):
        return self.obtener_informacion()
