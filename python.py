# Importamos el módulo datetime
import datetime 

# Importamos el módulo Colorama
from colorama import Fore, init 
init() 

productos = []
while True:
    print(Fore.CYAN + "\nSistema de Gestión Básica De Productos")
    print(Fore.WHITE + "\n1. Agregar producto")
    print(Fore.WHITE + "\n2. Mostrar productos")
    print(Fore.WHITE + "\n3. Buscar producto")
    print(Fore.WHITE + "\n4. Eliminar producto")
    print(Fore.WHITE + "\n5. Salir")
    print(Fore.WHITE + "\n")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría del producto: ")
        precio = float(input("Precio del producto: "))
        if precio < 0:
            print("ERROR! El precio no puede ser negativo.")
            continue
        precio = round(precio, 0)

        # Obtener el próximo código autonumérico
        try:
            with open("datos.txt", "r") as archivo:
                lineas = archivo.readlines()
                codigo = len(lineas) + 1
        except FileNotFoundError:
            codigo = 1  # Si el archivo no existe, empezamos desde 1

        #producto = {
        #    "nombre": nombre,
        #    "categoria": categoria,
        #    "precio": precio,
        #    "fechaRegistro": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #}
        #productos.append(producto)
        # Escribir los productos en un archivo
          
        archivo = open("datos.txt", "a") 
        archivo.write(str(codigo)+";"+nombre+";"+categoria+";"+str(precio)+";"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n") 
        archivo.close()    
        #print("Producto agregado exitosamente.")
        print(f"Producto agregado exitosamente. Código asignado: {codigo}")
    elif opcion == "2":
        # Leer y mostrar el contenido del archivo 
        archivo = open("datos.txt", "r") 
        print("\n--- Productos Registrados ---")
        for linea in archivo:
            codigo, nombre, categoria, precio, fecha = linea.strip().split(";") 
            print(f"Codigo: {codigo}, Nombre: {nombre}, Categoria: {categoria}, Precio: {precio}, Fecha de registro: {fecha}")
        archivo.close() 
        #productos.sort(key=lambda x: x["nombre"])
        #for i, producto in enumerate(productos, 1):
        #    print(f"Codigo: {i}, Nombre: {producto['nombre'].capitalize()}, Categoria: {producto['categoria'].capitalize()}, Precio: {producto['precio']}, Fecha de registro: {producto['fechaRegistro']}")
    elif opcion == "3":
        # Buscar un producto por nombre
        busqueda = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        archivo = open("datos.txt", "r") 
        print("\n--- Producto Registrado ---")

        for linea in archivo:
            codigo, nombre, categoria, precio, fecha = linea.strip().split(";") 
            #if producto["nombre"].lower() == busqueda.lower():
            #   print(f"Codigo: {i}, Nombre: {producto['nombre'].capitalize()}, Categoria: {producto['categoria'].capitalize()}, Precio: {producto['precio']} Fecha de registro: {producto['fechaRegistro']}")
            if codigo == busqueda:
                print(f"Codigo: {codigo}, Nombre: {nombre}, Categoria: {categoria}, Precio: {precio}, Fecha de registro: {fecha}")
                encontrado = True
                break 
            #print(linea.strip()) 
        archivo.close() 
        #for i, producto in enumerate(productos, 1):
        #    if producto["nombre"].lower() == busqueda.lower():
        #        print(f"Codigo: {i}, Nombre: {producto['nombre'].capitalize()}, Categoria: {producto['categoria'].capitalize()}, Precio: {producto['precio']} Fecha de registro: {producto['fechaRegistro']}")
        #        encontrado = True
        #        break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "4":
        # Eliminar un producto por nombre
        eliminar = input("Ingrese el código del producto a eliminar: ")
        eliminado = False
        #for i, producto in enumerate(productos, 1):
        #    if str(i) == eliminar:
        #        productos.pop(i-1)
        #        print("Producto eliminado exitosamente.")
        #        eliminado = True
        #        break
        # Leer todas las líneas
        with open("datos.txt", "r") as archivo:
            lineas = archivo.readlines()

        # Abrir el archivo en modo escritura para reescribirlo
        with open("datos.txt", "w") as archivo:
            for linea in lineas:
                codigo, nombre, categoria, precio, fecha = linea.strip().split(";")
                if codigo != eliminar:
                    archivo.write(linea)
                else:
                    eliminado = True
        #if not eliminado:
        #    print("Producto no encontrado.")
        if eliminado:
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")