import random  # Importar el módulo random para generar números aleatorios

class Cuenta:
    # Constructor de la clase Cuenta
    # Estas validaciones están ocultas para el usuario, quien solo ve un mensaje de error si intenta realizar una operación inválida.
    def __init__(self, titular, saldo):
        self.titular = titular
        self.numero_cuenta = self.generar_numero_cuenta()
        self._saldo = saldo  # Atributo protegido

    # Getter para _saldo
    @property
    def saldo(self):
        return self._saldo

    # Setter para _saldo
    #Aquí, el usuario no necesita saber cómo se genera el número de cuenta o cómo se valida el saldo. 
    #Solo interactúa con métodos públicos como depositar, retirar y mostrar_informacion.
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:  # Validación para evitar saldos negativos
            self._saldo = nuevo_saldo
        else:
            print("Error: El saldo no puede ser negativo.")

    # Método para generar un número de cuenta aleatorio de 16 dígitos
    def generar_numero_cuenta(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    # Método para depositar dinero en la cuenta
    #El usuario no necesita saber cómo se actualiza el saldo internamente; solo llama al método depositar y este se encarga de todo.
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo = self.saldo + cantidad  # Usa el setter para actualizar el saldo
            print(f"Depósito exitoso de {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad  # Usa el setter para actualizar el saldo
            print(f"Retiro exitoso de {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    # Método para mostrar la información de la cuenta
    def mostrar_informacion(self):
        return f"Titular: {self.titular}\nNúmero de cuenta: {self.numero_cuenta}\nSaldo: {self.saldo}"


# Clase CuentaAhorro que hereda de la clase Cuenta
class CuentaAhorro(Cuenta):
    def __init__(self, titular, saldo, tasa_interes):
        if saldo < 0:  # Validación para evitar saldos negativos al crear la cuenta
            raise ValueError("Error: El saldo inicial de una cuenta de ahorro no puede ser negativo.")
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes

    # Método para calcular el interés de la cuenta de ahorro
    # Aquí, el método calcular_interes es específico de CuentaAhorro, pero el usuario no necesita saber cómo se calcula el interés; solo llama al método.
    def calcular_interes(self):
        interes = self.saldo * self.tasa_interes  # Usa el getter para obtener el saldo
        self.saldo = self.saldo + interes  # Usa el setter para actualizar el saldo
        print(f"Interés de {interes} añadido a la cuenta de ahorro. Nuevo saldo: {self.saldo}")

    # Método para mostrar la información de la cuenta de ahorro
    def mostrar_informacion(self):
        return f"Tipo de cuenta: Ahorro\n{super().mostrar_informacion()}\nTasa de interés: {self.tasa_interes * 100}%"


# Clase CuentaMonetaria que hereda de la clase Cuenta
class CuentaMonetaria(Cuenta):
    def __init__(self, titular, saldo, limite_credito):
        if saldo < 0:  # Validación para evitar saldos negativos al crear la cuenta
            raise ValueError("Error: El saldo inicial de una cuenta monetaria no puede ser negativo.")
        super().__init__(titular, saldo)
        self.limite_credito = limite_credito

    # Método para retirar dinero de la cuenta monetaria
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= (self.saldo + self.limite_credito):
            self.saldo = self.saldo - cantidad  # Usa el setter para actualizar el saldo
            print(f"Retiro exitoso de {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    # Método para mostrar la información de la cuenta monetaria
    def mostrar_informacion(self):
        return f"Tipo de cuenta: Monetaria\n{super().mostrar_informacion()}\nLímite de crédito: {self.limite_credito}"


# Función para mostrar el menú principal del sistema bancario
# El usuario no necesita saber cómo se almacenan las cuentas o cómo se gestionan internamente;
# solo interactúa con opciones simples como "Abrir Cuenta" o "Gestionar Cuenta".
def menu_principal():
    # Lista para almacenar las cuentas creadas
    cuentas = []

    # Menú principal del sistema bancario
    while True:
        print("\n--- Menú Bancario ---")
        print("1. Abrir Cuenta")
        print("2. Gestionar Cuenta")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        # Opciones del menú principal del sistema bancario
        if opcion == "1":
            print("\n--- Abrir Cuenta ---")
            print("1. Cuenta de ahorro")
            print("2. Cuenta monetaria")
            print("3. Regresar")
            tipo_cuenta = input("Seleccione una opción: ")

            # Crear una cuenta de ahorro o monetaria
            if tipo_cuenta == "1":
                titular = input("Ingrese el nombre del titular: ")
                saldo = float(input("Ingrese el saldo inicial: "))
                tasa_interes = float(input("Ingrese la tasa de interés: "))
                try:
                    cuenta = CuentaAhorro(titular, saldo, tasa_interes)
                    cuentas.append(cuenta)
                    print(f"Cuenta de ahorro creada exitosamente. Número de cuenta: {cuenta.numero_cuenta}")
                except ValueError as e:
                    print(e)  # Muestra el mensaje de error si el saldo es negativo

            elif tipo_cuenta == "2":
                titular = input("Ingrese el nombre del titular: ")
                saldo = float(input("Ingrese el saldo inicial: "))
                limite_credito = float(input("Ingrese el límite de crédito: "))
                try:
                    cuenta = CuentaMonetaria(titular, saldo, limite_credito)
                    cuentas.append(cuenta)
                    print(f"Cuenta monetaria creada exitosamente. Número de cuenta: {cuenta.numero_cuenta}")
                except ValueError as e:
                    print(e)  # Muestra el mensaje de error si el saldo es negativo

            elif tipo_cuenta == "3":
                continue
            else:
                print("Opción inválida.")

        elif opcion == "2":
            if not cuentas:
                print("No hay cuentas creadas.")
                continue

            # Menú de gestión de cuentas
            print("\n--- Gestionar Cuenta ---")
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
            print("... Saliendo del sistema ...")
            break
        else:
            print("Opción inválida.")


# Ejecutar el menú principal del sistema bancario
if __name__ == "__main__":
    menu_principal()

# La abstracción en este código se logra al ocultar los detalles internos de las clases (Cuenta, CuentaAhorro, CuentaMonetaria) 
# y exponer solo una interfaz pública sencilla para interactuar con ellas. Esto permite que el usuario utilice las
# funcionalidades sin preocuparse por cómo están implementadas, lo que facilita el uso y mantenimiento del código.
