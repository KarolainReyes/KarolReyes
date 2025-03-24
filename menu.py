def menu_principal():
    menuPrincipal = """
    *************Bienvenido a la panaderia Bizcochito*************
    1. Cliente
    2. Empleado
    3. Salir
    **************************************************************
    """
    print(menuPrincipal)
    return input ("Por favor indique si usted es :")

def menu_clientes():
    menuClientes = """
    *************Bienvenido a la panaderia Bizcochito*************

    1. Ver los productos disponibles
    2. Realizar un pedido
    3. Modificar un pedido
    4. Eliminar un pedido
    5. Buscar
    6. Salir
    **************************************************************
    """
    print(menuClientes)
    return input ("Por favor seleccione la opción que desea :")

def menu_empleados ():
    menuEmpleados = """
    *************Bienvenido a la panaderia Bizcochito*************
    
    1. Registrar un nuevo producto
    2. Ver disponibilidad de Stock
    3. Modificar un producto
    4. Eliminar producto
    5. Buscar productos
    6. Buscar pedidos
    7. Salir
    **************************************************************
    """
    print(menuEmpleados)
    return input ("Por favor seleccione la opción que desea :")

    
def buscar_producto ():
    buscarProducto = """
    *************Bienvenido a la panaderia Bizcochito*************
    1. Nombre
    2. Categoria
    3. Codigo
    4. Salir

    **************************************************************
    """
    print(buscarProducto)
    return input ("Por favor indique el metodo de busqueda :")

def busqueda_pedido ():
    busquedaPedido = """
    *************Bienvenido a la panaderia Bizcochito*************
    
    1. Codigo de pedido
    2. Codigo de cliente
    3. Fecha de pedido
    4. Salir
    **************************************************************
    """
    print(busquedaPedido)
    return input ("Por favor seleccione la opción de búsqueda que desea realizar: :")
