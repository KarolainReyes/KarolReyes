import json
from menu import *
from funcionesEmpleados import prodisponibles, productos_disp, escribir_productos, escribir_pedidos, leer_pedidos, leerjson
def pedir_op_cliente():
        while True:
            opc=menu_clientes()
            if opc == "1":
                disponibles_clientes()
            elif opc == "2":
                realizar_pedidos()
            elif opc == "3":
                modificar_pedidos()
            elif opc == "4":
                eliminar_pedido()
            elif opc == "5":
                 while True:
                     op=buscar_producto()
                     if op=="1":
                         buscar_por_nombre()
                     elif op=="2":
                         buscar_por_categoria()
                     elif op=="3":
                         buscar_por_codigo()
                     elif op=="4":
                         print("Saliendo")
                         break
                     else:print("Ingrese una opcion valida")
                      
            elif opc=="6":
                print("Saliendo")
                break
            else:
                print("Porfavor ingrese una opción válida")



def disponibles_clientes():
    with open ("productos.json", "r") as file:
        data = json.load(file)
    for producto in data:
        print("************************")
        for clave, valor in producto.items():
            if clave=="codigo_producto":
                print(f"Codigo->{valor}")
            elif clave=="nombre":
                print(f"{clave}->{valor}")
            elif clave=="descripcion":
                print(f"{clave}->{valor}")
            elif clave=="cantidad_en_stock":
                print(f"{clave}->{valor}")
            elif clave=="precio_venta":
                print(f"{clave}->{valor}")

def realizar_pedidos():
    global proddisp
    with open("codigopedido.json","r") as file:
        numero_pedido=json.load(file)
    codigo_cliente=input("Ingrese el codigo del cliente: ")
    fecha_pedido=input("Ingrese la fecha del pedido (YYYY-MM-DD): ")
    productos_pedido=[]
    numero_linea=1
    while True:
        productoexistente=False
        dosprod=input("Desea añadir un producto?Y/N: ").lower()
        if dosprod=="y":    
            agregar=input("Ingrese codigo/nombre del producto: ")
            for producto in prodisponibles:
                if producto["codigo_producto"]==agregar:
                    productoexistente=True
                    indice=prodisponibles.index(producto)
                if producto["nombre"]==agregar:
                    productoexistente=True
                    indice=prodisponibles.index(producto)
            if productoexistente==True:
                cantidad=int(input("¿Que cantidad desea comprar?: "))
                if cantidad<=prodisponibles[indice]["cantidad_en_stock"]:
                    prodisponibles[indice]["cantidad_en_stock"]-=cantidad
                    escribir_productos()
                    productos_pedido.append({"codigo_producto":prodisponibles[indice]["codigo_producto"],
                                            "nombre":prodisponibles[indice]["nombre"],
                                            "cantidad":cantidad,
                                            "precio":prodisponibles[indice]["precio_venta"],
                                            "numero_linea":numero_linea})
                    numero_linea+=1
                    print("Producto añadido exitosamente")
                    dosprod=input("Desea añadir otro producto? Y/N: ").lower()
                    if dosprod=="n":
                        print("Añadiendo productos...")
                        pedidos=leer_pedidos()
                        pedidos.append({"codigo_pedido":numero_pedido[0],
                                        "codigo_cliente":codigo_cliente,
                                        "fecha_pedido":fecha_pedido,
                                        "detalles_pedido":productos_pedido})
                        with open("pedidos.json","w")as file:
                            json.dump(pedidos, file, indent=4)
                        numero_pedido[0]+=1
                        print("Pedido añadido correctamente")
                        with open("codigopedido.json","w")as file:
                            json.dump(numero_pedido,file)
                        break
                    if dosprod!="y" and dosprod!="n":
                        print("Ingrese una opcion valida")
                else: print("Cantidad deseada no disponible")
            else: print("El producto ingresado no existe")
        if dosprod=="n":
                        print("Añadiendo productos...")
                        pedidos=leer_pedidos()
                        pedidos.append({"codigo_pedido":numero_pedido[0],
                                        "codigo_cliente":codigo_cliente,
                                        "fecha_pedido":fecha_pedido,
                                        "detalles_pedido":productos_pedido})
                        with open("pedidos.json","w")as file:
                            json.dump(pedidos, file, indent=4)
                        numero_pedido[0]+=1
                        print("Pedido añadido correctamente")
                        with open("codigopedido.json","w")as file:
                            json.dump(numero_pedido,file)
                        break    
        else:print("Ingrese una opciòn valida")

def modificar_pedidos():
    pedidoexiste=False
    pedidos=leer_pedidos()
    codigopedido=int(input("Ingrese codigo del pedido"))
    for pedido in pedidos:
        if pedido["codigo_pedido"]==codigopedido:
            pedidoexiste=True
            indicepedido=pedidos.index(pedido)
    if pedidoexiste==True:
        codigo_cliente=input("Ingrese el codigo del cliente: ")
        fecha_pedido=input("Ingrese la fecha del pedido (YYYY-MM-DD): ")
        productos_pedido=[]
        numero_linea=1
        while True:
            productoexistente=False
            dosprod=input("Desea añadir un producto?Y/N: ").lower()
            if dosprod=="y":    
                agregar=input("Ingrese codigo/nombre del producto: ")
                for producto in prodisponibles:
                    if producto["codigo_producto"]==agregar:
                        productoexistente=True
                        indice=prodisponibles.index(producto)
                    if producto["nombre"]==agregar:
                        productoexistente=True
                        indice=prodisponibles.index(producto)
                if productoexistente==True:
                    cantidad=int(input("¿Que cantidad desea comprar?: "))
                    if cantidad<=prodisponibles[indice]["cantidad_en_stock"]:
                        prodisponibles[indice]["cantidad_en_stock"]-=cantidad
                        escribir_productos()
                        productos_pedido.append({"codigo_producto":prodisponibles[indice]["codigo_producto"],
                                                "nombre":prodisponibles[indice]["nombre"],
                                                "cantidad":cantidad,
                                                "precio":prodisponibles[indice]["precio_venta"],
                                                "numero_linea":numero_linea})
                        numero_linea+=1
                        print("Producto añadido exitosamente")
                        dosprod=input("Desea añadir otro producto? Y/N: ").lower()
                        if dosprod=="n":
                            print("Añadiendo productos...")
                            pedidos=leer_pedidos()
                            pedidos[indicepedido]={"codigo_pedido":codigopedido,
                                            "codigo_cliente":codigo_cliente,
                                            "fecha_pedido":fecha_pedido,
                                            "detalles_pedido":productos_pedido}
                            with open("pedidos.json","w")as file:
                                json.dump(pedidos, file, indent=4)
                            print("Pedido añadido correctamente")
                            break
                        if dosprod!="y" and dosprod!="n":
                            print("Ingrese una opcion valida")
                    else: print("Cantidad deseada no disponible")
                else: print("El producto ingresado no existe")
            if dosprod=="n":
                            print("Añadiendo productos...")
                            pedidos=leer_pedidos()
                            pedidos[indicepedido]={"codigo_pedido":codigopedido,
                                            "codigo_cliente":codigo_cliente,
                                            "fecha_pedido":fecha_pedido,
                                            "detalles_pedido":productos_pedido}
                            with open("pedidos.json","w")as file:
                                json.dump(pedidos, file, indent=4)
                            print("Pedido añadido correctamente")
                            break    
            else:print("Ingrese una opciòn valida")
    else: print("El pedido no existe")

def eliminar_pedido():
     pedidos=leer_pedidos()
     pedidoexiste=False
     codigopedido=int(input("Ingrese el codigo del pedido a eliminar: "))
     for pedido in pedidos:
          if pedido["codigo_pedido"]==codigopedido:
               indice=pedidos.index(pedido)
               pedidoexiste=True
               pedidos.pop(indice)
               with open("pedidos.json","w")as file:
                    json.dump(pedidos,file, indent=4)
               print("El pedido ha sido eliminado con exito")
     if pedidoexiste==False:
          print("El pedido ingresado no existe")

def buscar_por_codigo():
    productos=leerjson()
    productoexiste=False
    codigoproducto=input("Ingrese el codigo del producto: ")
    for producto in productos:
         if producto["codigo_producto"]==codigoproducto:
              print("************************")
              productoexiste=True
              for clave, valor in producto.items():
                   if clave!="proveedor" and clave!="precio_proveedor":
                        print(f"{clave}->{valor}")
                   
    if productoexiste==False: print("El producto ingresado no existe")
     
def buscar_por_nombre():
    productos=leerjson()
    productoexiste=False
    nombreproducto=input("Ingrese el nombre del producto: ")
    for producto in productos:
         if producto["nombre"]==nombreproducto:
              productoexiste=True
              print("************************")
              for clave, valor in producto.items():
                   if clave!="proveedor" and clave!="precio_proveedor":
                        print(f"{clave}->{valor}")
                   
    if productoexiste==False: print("El producto ingresado no existe")

def buscar_por_categoria():
    productos=leerjson()
    productoexiste=False
    categoriaproducto=input("Ingrese la categoria del producto: ")
    for producto in productos:
         if producto["categoria"]==categoriaproducto:
              productoexiste=True
              print("************************")
              for clave, valor in producto.items():
                   if clave!="proveedor" and clave!="precio_proveedor":
                        print(f"{clave}->{valor}")
                   
    if productoexiste==False: print("El producto ingresado no existe")