# crypto_tracker/módulos/cartera.py

class Cartera:
    def __init__(self):
        self.monedas = []

    def agregar_moneda(self, moneda):
        if self._moneda_no_existente(moneda):
            self.monedas.append(moneda)
            print(f"¡{moneda.nombre} ha sido agregada a tu cartera!")
        else:
            print(f"{moneda.nombre} ya está en tu cartera. No se agregará.")

    def eliminar_moneda(self, moneda):
        if moneda in self.monedas:
            self.monedas.remove(moneda)
            print(f"¡{moneda.nombre} ha sido eliminada de tu cartera!")
        else:
            print(f"{moneda.nombre} no está en tu cartera. No se eliminará.")

    def valor_total(self):
        return sum(moneda.precio for moneda in self.monedas)

    def _moneda_no_existente(self, moneda):
        return moneda not in self.monedas

    def __str__(self):
        if not self.monedas:
            return "Tu cartera está vacía."
        
        return "\n".join(str(moneda) for moneda in self.monedas) + f"\n\nValor Total de la Cartera: ${self.valor_total():.2f}"

