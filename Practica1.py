import random # Importar el módulo random para generar números aleatorios

class Cuenta:
    # Constructor de la clase Cuenta
    # Genera un número de cuenta aleatorio de 16 dígitos
    def __init__(self, titular, saldo):
        self.titular = titular
        self.numero_cuenta = self.generar_numero_cuenta()
        self._saldo = saldo

    # Método para generar un número de cuenta aleatorio de 16 dígitos
    def generar_numero_cuenta(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    # Métodos de la clase Cuenta
    # Metodo para depositar dinero en la cuenta
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito exitoso de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro exitoso de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    #Metodo para mostrar el saldo de la cuenta
    def mostrar_saldo(self):
        return self._saldo

    # Método para mostrar la información de la cuenta
    def mostrar_informacion(self):
        return f"Titular: {self.titular}\nNúmero de cuenta: {self.numero_cuenta}\nSaldo: {self._saldo}"

# Clase CuentaAhorro que hereda de la clase Cuenta y añade un atributo tasa_interes
# y un método calcular_interes
class CuentaAhorro(Cuenta):
    # Constructor de la clase CuentaAhorro
    # Recibe la tasa de interés como parámetro al crear la cuenta ahorro
    # El saldo inicial es 0 y la tasa de interés es 0.05 (5%) por defecto
    # El titular y el saldo se pasan al constructor de la clase Cuenta
    def __init__(self, titular, saldo, tasa_interes):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes

    # Método para calcular el interés de la cuenta de ahorro
    # Añade el interés al saldo de la cuenta y muestra un mensaje con el nuevo saldo y el interés añadido
    def calcular_interes(self):
        interes = self._saldo * self.tasa_interes
        self._saldo += interes
        print(f"Interés de {interes} añadido a la cuenta de ahorro. Nuevo saldo: {self._saldo}")

    # Método para mostrar la información de la cuenta de ahorro
    # Añade la tasa de interés al mensaje de información
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}\nTasa de interés: {self.tasa_interes * 100}%"

# Clase CuentaMonetaria para cuentas con límite de crédito
# Hereda de la clase Cuenta y añade un atributo limite_credito
class CuentaMonetaria(Cuenta):
    # Constructor de la clase CuentaMonetaria
    # Recibe el límite de crédito como parámetro al crear la cuenta monetaria y el saldo inicial
    # El titular y el saldo se pasan al constructor de la clase Cuenta
    def __init__(self, titular, saldo, limite_credito):
        super().__init__(titular, saldo)
        self.limite_credito = limite_credito

    # Método para retirar dinero de la cuenta monetaria
    # Si la cantidad a retirar es mayor que el saldo y el límite de crédito, muestra un mensaje de error
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= (self._saldo + self.limite_credito):
            self._saldo -= cantidad
            print(f"Retiro exitoso de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    # Método para mostrar la información de la cuenta monetaria
    # Añade el límite de crédito al mensaje de información
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}\nLímite de crédito: {self.limite_credito}"

# Función para mostrar el menú principal del sistema bancario
# Permite abrir cuentas de ahorro y monetarias, gestionar cuentas, depositar, retirar y calcular interés
def menu_principal():
    # Lista para almacenar las cuentas creadas
    cuentas = []

    # Menu principal del sistema bancario
    while True:
        print("\n---Menu Bancario---")
        print("1. Abrir Cuenta")
        print("2. Gestionar Cuenta")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        # Opciones del menú principal del sistema bancario
        if opcion == "1":
            print("\n---Menu Bancario---")
            print("1. Cuenta de ahorro")
            print("2. Cuenta monetaria")
            print("3. Regresar")
            tipo_cuenta = input("Seleccione una opción: ")

            # Crear una cuenta de ahorro o monetaria y añadirla a la lista de cuentas creadas si se selecciona la opción 1 o 2 de la lista de cuentas creadas
            if tipo_cuenta == "1":
                titular = input("Ingrese el nombre del titular: ")
                saldo = float(input("Ingrese el saldo inicial: "))
                tasa_interes = float(input("Ingrese la tasa de interés: "))
                cuenta = CuentaAhorro(titular, saldo, tasa_interes)
                cuentas.append(cuenta)
                print(f"Cuenta de ahorro creada exitosamente. Número de cuenta: {cuenta.numero_cuenta}")

            # Crear una cuenta monetaria y añadirla a la lista de cuentas creadas si se selecciona la opción 2 de la lista de cuentas creadas
            elif tipo_cuenta == "2":
                titular = input("Ingrese el nombre del titular: ")
                saldo = float(input("Ingrese el saldo inicial: "))
                limite_credito = float(input("Ingrese el límite de crédito: "))
                cuenta = CuentaMonetaria(titular, saldo, limite_credito)
                cuentas.append(cuenta)
                print(f"Cuenta monetaria creada exitosamente. Número de cuenta: {cuenta.numero_cuenta}")

            # Regresar al menú principal si se selecciona la opción 3 de la lista de cuentas creadas
            elif tipo_cuenta == "3":
                continue
            # Mostrar un mensaje de error si se selecciona una opción inválida
            else:
                print("Opción inválida.")

        # Gestionar cuentas si se seleccion
        elif opcion == "2":
            if not cuentas:
                print("No hay cuentas creadas.")
                continue

            # Menú de gestión de cuentas
            print("\n---Menu Bancario---")
            print("1. Ver información de cuentas")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Calcular interés (Solo Cuenta de Ahorro)")
            print("5. Regresar")
            gestion_opcion = input("Seleccione una opción: ")

            # Opciones de gestión de cuentas
            if gestion_opcion == "1":
                for cuenta in cuentas:
                    print(cuenta.mostrar_informacion())
                    print("-------------------")

            # Depositar dinero en una cuenta si se selecciona la opción 2 de la lista de gestión de cuentas
            elif gestion_opcion == "2":
                tipo_cuenta = input("¿En qué cuenta desea depositar? (ahorro/monetaria): ").lower()
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                for cuenta in cuentas:
                    if (tipo_cuenta == "ahorro" and isinstance(cuenta, CuentaAhorro)) or (tipo_cuenta == "monetaria" and isinstance(cuenta, CuentaMonetaria)):
                        cuenta.depositar(cantidad)
                        break
                    # Mostrar un mensaje de error si no se encuentra una cuenta del tipo especificado
                else:
                    print("No se encontró una cuenta del tipo especificado.")

            # Retirar dinero de una cuenta si se selecciona la opción 3 de la lista de gestión de cuentas
            elif gestion_opcion == "3":
                tipo_cuenta = input("¿De qué cuenta desea retirar? (ahorro/monetaria): ").lower()
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                for cuenta in cuentas:
                    if (tipo_cuenta == "ahorro" and isinstance(cuenta, CuentaAhorro)) or (tipo_cuenta == "monetaria" and isinstance(cuenta, CuentaMonetaria)):
                        cuenta.retirar(cantidad)
                        break
                    # Mostrar un mensaje de error si no se encuentra una cuenta del tipo especificado
                else:
                    print("No se encontró una cuenta del tipo especificado.")

            # Calcular el interés de una cuenta de ahorro si se selecciona la opción 4 de la lista de gestión de cuentas
            elif gestion_opcion == "4":
                for cuenta in cuentas:
                    if isinstance(cuenta, CuentaAhorro):
                        cuenta.calcular_interes()
                        break
                    # Mostrar un mensaje de error si no se encuentra una cuenta de ahorro
                else:
                    print("No hay cuentas de ahorro para calcular el interés.")

            # Regresar al menú principal si se selecciona la opción 5 de la lista de gestión de cuentas
            elif gestion_opcion == "5":
                continue
            # Mostrar un mensaje de error si se selecciona una opción inválida
            else:
                print("Opción inválida.")

        # Salir del sistema si se seleccion
        elif opcion == "3":
            print("...Saliendo del sistema...")
            break
        # Mostrar un mensaje de error si se selecciona una opción inválida
        else:
            print("Opción inválida.")

# Ejecutar el menú principal del sistema bancario si se ejecuta el script
if __name__ == "__main__":
    menu_principal()
