from menu import menu_principal, menu_empleados
from funcionesClientes import *
from funcionesEmpleados import *

while True:
    op = menu_principal()
    match op:
        case "1":
                pedir_op_cliente()
        case "2":   
                pedir_opc_empleado()
        case "3":
            print("saliendo...")
            print("Gracias por usar nuestro sistema")
            break   
        case _:
            print("Ingrese una opcion valida")