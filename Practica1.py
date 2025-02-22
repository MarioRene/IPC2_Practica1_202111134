import random

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.numero_cuenta = self.generar_numero_cuenta()
        self._saldo = saldo

    def generar_numero_cuenta(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

        def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito exitoso de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro exitoso de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def mostrar_saldo(self):
        return self._saldo

    def mostrar_informacion(self):
        return f"Titular: {self.titular}\nNúmero de cuenta: {self.numero_cuenta}\nSaldo: {self._saldo}"

class CuentaAhorro(Cuenta):
    def __init__(self, titular, saldo, tasa_interes):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes

    def calcular_interes(self):
        interes = self._saldo * self.tasa_interes
        self._saldo += interes
        print(f"Interés de {interes} añadido a la cuenta de ahorro. Nuevo saldo: {self._saldo}")

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}\nTasa de interés: {self.tasa_interes * 100}%"

class CuentaMonetaria(Cuenta):
    def __init__(self, titular, saldo, limite_credito):
        super().__init__(titular, saldo)
        self.limite_credito = limite_credito

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= (self._saldo + self.limite_credito):
            self._saldo -= cantidad
            print(f"Retiro exitoso de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}\nLímite de crédito: {self.limite_credito}"


