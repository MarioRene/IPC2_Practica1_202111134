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

    def menu_principal():
    cuentas = []
    while True:
        print("\n---Menu Bancario---")
        print("1. Abrir Cuenta")
        print("2. Gestionar Cuenta")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n---Menu Bancario---")
            print("1. Cuenta de ahorro")
            print("2. Cuenta monetaria")
            print("3. Regresar")
            tipo_cuenta = input("Seleccione una opción: ")

            if tipo_cuenta == "1":
                titular = input("Ingrese el nombre del titular: ")
                saldo = float(input("Ingrese el saldo inicial: "))
                tasa_interes = float(input("Ingrese la tasa de interés: "))
                cuenta = CuentaAhorro(titular, saldo, tasa_interes)
                cuentas.append(cuenta)
                print(f"Cuenta de ahorro creada exitosamente. Número de cuenta: {cuenta.numero_cuenta}")

            elif tipo_cuenta == "2":
                titular = input("Ingrese el nombre del titular: ")
                saldo = float(input("Ingrese el saldo inicial: "))
                limite_credito = float(input("Ingrese el límite de crédito: "))
                cuenta = CuentaMonetaria(titular, saldo, limite_credito)
                cuentas.append(cuenta)
                print(f"Cuenta monetaria creada exitosamente. Número de cuenta: {cuenta.numero_cuenta}")

            elif tipo_cuenta == "3":
                continue
            else:
                print("Opción inválida.")

        elif opcion == "2":
            if not cuentas:
                print("No hay cuentas creadas.")
                continue

            print("\n---Menu Bancario---")
            print("1. Ver información de cuentas")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Calcular interés (Solo Cuenta de Ahorro)")
            print("5. Regresar")
            gestion_opcion = input("Seleccione una opción: ")

            if gestion_opcion == "1":
                for cuenta in cuentas:
                    print(cuenta.mostrar_informacion())
                    print("-------------------")

            elif gestion_opcion == "2":
                tipo_cuenta = input("¿En qué cuenta desea depositar? (ahorro/monetaria): ").lower()
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                for cuenta in cuentas:
                    if (tipo_cuenta == "ahorro" and isinstance(cuenta, CuentaAhorro)) or (tipo_cuenta == "monetaria" and isinstance(cuenta, CuentaMonetaria)):
                        cuenta.depositar(cantidad)
                        break
                else:
                    print("No se encontró una cuenta del tipo especificado.")

            elif gestion_opcion == "3":
                tipo_cuenta = input("¿De qué cuenta desea retirar? (ahorro/monetaria): ").lower()
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                for cuenta in cuentas:
                    if (tipo_cuenta == "ahorro" and isinstance(cuenta, CuentaAhorro)) or (tipo_cuenta == "monetaria" and isinstance(cuenta, CuentaMonetaria)):
                        cuenta.retirar(cantidad)
                        break
                else:
                    print("No se encontró una cuenta del tipo especificado.")

            elif gestion_opcion == "4":
                for cuenta in cuentas:
                    if isinstance(cuenta, CuentaAhorro):
                        cuenta.calcular_interes()
                        break
                else:
                    print("No hay cuentas de ahorro para calcular el interés.")

            elif gestion_opcion == "5":
                continue
            else:
                print("Opción inválida.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()

