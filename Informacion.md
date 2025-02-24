#Implementación de Abstracción
-Creación de clase abstracta:
  -No se crea una clase abstracta explícita (no se usa abc.ABC), pero la clase Cuenta actúa como una abstracción al definir una interfaz común para todas las cuentas bancarias, ocultando los detalles de implementación.

#Implementación de Herencia
-Herencia en atributos:
  -Las clases CuentaAhorro y CuentaMonetaria heredan atributos como titular, numero_cuenta y _saldo de la clase Cuenta.

-Herencia en métodos:
  -Las clases derivadas heredan métodos como depositar, retirar y mostrar_informacion de la clase Cuenta, y pueden extenderlos o sobrescribirlos.

#Implementación de Encapsulamiento
-Atributos privados:
  -El atributo _saldo se marca como protegido (con un guion bajo _) para indicar que no debe ser accedido directamente desde fuera de la clase.

-Uso de getters:
  -El método mostrar_saldo actúa como un getter para acceder al valor de _saldo.

-Uso de setters:
  -No se implementan setters explícitos, pero los métodos depositar y retirar modifican _saldo de manera controlada.

#Implementación de Polimorfismo
-Sobrescritura de métodos:
  -La clase CuentaMonetaria sobrescribe el método retirar para incluir la lógica del límite de crédito.
  -Las clases CuentaAhorro y CuentaMonetaria extienden el método mostrar_informacion para añadir información específica de cada tipo de cuenta.
