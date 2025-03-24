import json
from menu import *

global archivo_json, prodisponibles
lecturajson="productos.json"

def registrar_producto():
        global lecturajson
        with open (lecturajson, "r") as file:
            prodisponibles = json.load(file)
        codigo = input("Ingrese el código del producto: ")
        existe = False
        for x in prodisponibles:
          for cod in x.values():
            if cod == codigo:
             existe = True
            
        if existe == True:
            print("Este producto ya está registrado, porfavor ingrese uno nuevo")
        else:
            
            nom_producto=input("Ingrese el nombre del producto: ")
            categoria=input("Ingrese la categoria del producto: ")
            descrip=input("Ingrese la descripción del prducto: ")
            prov=input("Ingrese el nombre del proovedor: ")
            cant_stock=int(input("Ingrese el número de unidades disponibles: "))
            precio_venta=int(input("Ingrese el precio de venta al público: "))
            precio_proveedor=int(input("Ingrese el precio de compra: "))
            newprod= {  "codigo_producto" : codigo,
                        "nombre" : nom_producto,
                        "categoria" :categoria,
                        "descripcion" : descrip,
                        "proveedor" :prov,
                        "cantidad_en_stock" : cant_stock,
                        "precio_venta" : precio_venta,
                        "precio_proveedor" : precio_proveedor,}

            prodisponibles.append(newprod)
            with open("productos.json", "w") as file:
                json.dump(prodisponibles, file, indent=4)
                print("Producto registrado con éxito!")

def productos_disp():
     with open ("productos.json", "r") as file:
            pdisponibles = json.load(file)
     for producto in pdisponibles:
         print("************")
         for clave, valor in producto.items():
             print(f"{clave}->{valor}")
         if producto["cantidad_en_stock"]<10:
                print("El producto esta proximo a agotarse")
             

def mod_producto():
        global lecturajson
        global prodisponibles
        codigo=input("Ingrese el codigo del producto que desea modificar: ")
        existe = False
        for producto in prodisponibles:
            if producto["codigo_producto"]==codigo:
                indice=prodisponibles.index(producto)
                existe = True
        if existe == True:
            nom_producto=input("Ingrese el nombre del producto: ")
            categoria=input("Ingrese la categoria del producto: ")
            descrip=input("Ingrese la descripción del prducto: ")
            prov=input("Ingrese el nombre del proovedor: ")
            cant_stock=int(input("Ingrese el número de unidades disponibles: "))
            precio_venta=int(input("Ingrese el precio de venta al público: "))
            precio_proveedor=int(input("Ingrese el precio de compra: "))
            newprod= {  "codigo_producto" : codigo,
                    "nombre" : nom_producto,
                    "categoria" :categoria,
                    "descripcion" : descrip,
                    "proveedor" :prov,
                    "cantidad_en_stock" : cant_stock,
                    "precio_venta" : precio_venta,
                    "precio_proveedor" : precio_proveedor,}
            prodisponibles[indice]=newprod
            with open(lecturajson,"w") as file:
                json.dump(prodisponibles, file, indent=4)
                print("El producto fue modificado con exito")
        else: print("El producto no existe")

def eliminar_producto():
    global lecturajson
    global prodisponibles
    eliminado=0
    codigo =input("Ingrese el codigo del producto que desea eliminar")
    for producto in prodisponibles:
        for value in producto.values():
            if value == codigo:
                indice = prodisponibles.index(producto)
                del prodisponibles[indice]
                print("El producto se ha eliminado correctamente")
                eliminado = True
    if eliminado == False:
        print("El producto que usted ingreso no existe")
    with open (lecturajson, "w") as file:
        json.dump(prodisponibles, file, indent=4)

def leerjson():
    global archivo_json
    with open (archivo_json, "r") as file:
             pr=json.load(file)
    return pr


archivo_json = "productos.json"
prodisponibles=leerjson()

def pedir_opc_empleado():
    while True:
        op=menu_empleados()
        match op:
            case "1":
                registrar_producto()
            case "2":
                productos_disp()
            case "3":
                mod_producto()
            case "4":
                eliminar_producto()
            case "5":
                buscar_producto_empleados()
            case "6":
                buscar_pedidos()
            case "7":
                print("Saliendo")
                break
            case _:
                print("Ingrese una opción válida")

def escribir_productos():
    with open(archivo_json,"w") as file:
        json.dump(prodisponibles,file,indent=4)

def escribir_pedidos():
    with open("pedidos.json","w") as file:
        json.dump(pedidos,file, indent=4)

def leer_pedidos():
    with open("pedidos.json","r") as file:
        jsonpedido=json.load(file)
    return jsonpedido

pedidos=leer_pedidos()

def empleados_buscar_por_codigo():
    productos=leerjson()
    productoexiste=False
    codigoproducto=input("Ingrese el codigo del producto: ")
    for producto in productos:
         if producto["codigo_producto"]==codigoproducto:
              print("************************")
              productoexiste=True
              for clave, valor in producto.items():
                    print(f"{clave}->{valor}")
              if producto["cantidad_en_stock"]<10:
                print("El producto esta proximo a agotarse")
                   
    if productoexiste==False: print("El producto ingresado no existe")
     
def empleados_buscar_por_nombre():
    productos=leerjson()
    productoexiste=False
    nombreproducto=input("Ingrese el nombre del producto: ")
    for producto in productos:
         if producto["nombre"]==nombreproducto:
              productoexiste=True
              print("************************")
              for clave, valor in producto.items():
                        print(f"{clave}->{valor}")
              if producto["cantidad_en_stock"]<10:
                print("El producto esta proximo a agotarse")
                   
    if productoexiste==False: print("El producto ingresado no existe")

def empleados_buscar_por_categoria():
    productos=leerjson()
    productoexiste=False
    categoriaproducto=input("Ingrese la categoria del producto: ")
    for producto in productos:
         if producto["categoria"]==categoriaproducto:
              productoexiste=True
              print("************************")
              for clave, valor in producto.items():
                        print(f"{clave}->{valor}")
              if producto["cantidad_en_stock"]<10:
                print("El producto esta proximo a agotarse")
                   
    if productoexiste==False: print("El producto ingresado no existe")

def buscar_producto_empleados():
    while True:
     op=buscar_producto()
     if op=="1":
          empleados_buscar_por_nombre()
     elif op=="2":
          empleados_buscar_por_categoria()
     elif op=="3":
          empleados_buscar_por_codigo()
     elif op=="4":
          print("Saliendo")
          break
     else: print("Ingrese una opciòn valida")
    
def buscar_pedidos():
    while True:
     op=busqueda_pedido()
     if op=="1":
          buscar_pedido_codigo()
     elif op=="2":
          buscar_pedido_codigo_cliente()
     elif op=="3":
          buscar_pedido_fecha()
     elif op=="4":
          print("Saliendo")
          break
     else:print("Ingrese una opcion valida")

def buscar_pedido_codigo():
    existe=False
    codigo=int(input("Ingrese el codigo del pedido: "))
    for pedido in pedidos:
        if pedido["codigo_pedido"]==codigo:
            existe=True
            print("*****************")
            for clave, valor in pedido.items():
                if clave!="detalles_pedido":
                    print(f"{clave}---{valor}")
                elif clave=="detalles_pedido":
                    print(clave)
                    for pedido2 in valor:
                        print("---------------------")
                        for clave2, valor2 in pedido2.items():
                            print(f"{clave2}->{valor2}")
    if existe==False:print("El pedido no existe")

def buscar_pedido_codigo_cliente():
    existe=False
    codigocliente=input("Ingrese el codigo del cliente: ")
    for pedido in pedidos:
        if pedido["codigo_cliente"]==codigocliente:
            existe=True
            print("*****************")
            for clave, valor in pedido.items():
                if clave!="detalles_pedido":
                    print(f"{clave}---{valor}")
                elif clave=="detalles_pedido":
                    print(clave)
                    for pedido2 in valor:
                        print("---------------------")
                        for clave2, valor2 in pedido2.items():
                            print(f"{clave2}->{valor2}")
    if existe==False:print("El pedido no existe")

def buscar_pedido_fecha():
    existe=False
    fechapedido=input("Ingrese la fecha del pedido: ")
    for pedido in pedidos:
        if pedido["fecha_pedido"]==fechapedido:
            existe=True
            print("*****************")
            for clave, valor in pedido.items():
                if clave!="detalles_pedido":
                    print(f"{clave}---{valor}")
                elif clave=="detalles_pedido":
                    print(clave)
                    for pedido2 in valor:
                        print("---------------------")
                        for clave2, valor2 in pedido2.items():
                            print(f"{clave2}->{valor2}")
    if existe==False:print("El pedido no existe")    