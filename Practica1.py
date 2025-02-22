import random

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.numero_cuenta = self.generar_numero_cuenta()
        self._saldo = saldo

    def generar_numero_cuenta(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

