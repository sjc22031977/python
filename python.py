#productos = []

import datetime
from colorama import Fore, init
init()

import sqlite3

# Crear base y tabla
conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio REAL NOT NULL,
        fechaRegistro TEXT NOT NULL
   )
''')

conexion.commit()
conexion.close()

while True:
    print(Fore.CYAN + "\nSistema de Gestión Básica De Productos")
    print(Fore.WHITE + "\n1. Agregar producto")
    print(Fore.WHITE + "\n2. Mostrar productos")
    print(Fore.WHITE + "\n3. Buscar producto")
    print(Fore.WHITE + "\n4. Eliminar producto")
    print(Fore.WHITE + "\n5. Salir\n")

    opcion = input("Seleccione una opción: ")

    # ---------------- OPCIÓN 1: AGREGAR ----------------
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría del producto: ")
        precio = float(input("Precio del producto: "))

        if precio < 0:
            print("ERROR! El precio no puede ser negativo.")
            continue

        precio = round(precio, 0)

        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        cursor.execute('''
            INSERT INTO productos (nombre, categoria, precio, fechaRegistro)
            VALUES (?, ?, ?, ?)
        ''', (nombre, categoria, precio, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        conexion.commit()
        conexion.close()

        print("Producto agregado exitosamente.")

        #producto = {
        #    "nombre": nombre,
        #    "categoria": categoria,
        #    "precio": precio,
        #    "fechaRegistro": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #}
        #productos.append(producto)
        # Escribir los productos en un archivo
          
        #archivo = open("datos.txt", "a") 
        #archivo.write(str(codigo)+";"+nombre+";"+categoria+";"+str(precio)+";"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n") 
        #archivo.close()    
        #print("Producto agregado exitosamente.")
        #print(f"Producto agregado exitosamente. Código asignado: {codigo}")

    # ---------------- OPCIÓN 2: MOSTRAR ----------------
    elif opcion == "2":
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

        print("\n--- Productos Registrados ---")
        for p in productos:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Categoria: {p[2]}, Precio: {p[3]}, Fecha: {p[4]}")

        conexion.close()

        #productos.sort(key=lambda x: x["nombre"])
        #for i, producto in enumerate(productos, 1):
        #    print(f"Codigo: {i}, Nombre: {producto['nombre'].capitalize()}, Categoria: {producto['categoria'].capitalize()}, Precio: {producto['precio']}, Fecha de registro: {producto['fechaRegistro']}")

    # ---------------- OPCIÓN 3: BUSCAR ----------------
    elif opcion == "3":
        busqueda = input("Ingrese el nombre del producto a buscar: ")

        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos WHERE LOWER(nombre) = LOWER(?)", (busqueda,))
        producto = cursor.fetchone()

        if producto:
            print("\n--- Producto Encontrado ---")
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Categoria: {producto[2]}, Precio: {producto[3]}, Fecha: {producto[4]}")
        else:
            print("Producto no encontrado.")

        conexion.close()

        #for linea in archivo:
        #    codigo, nombre, categoria, precio, fecha = linea.strip().split(";") 
            #if producto["nombre"].lower() == busqueda.lower():
            #   print(f"Codigo: {i}, Nombre: {producto['nombre'].capitalize()}, Categoria: {producto['categoria'].capitalize()}, Precio: {producto['precio']} Fecha de registro: {producto['fechaRegistro']}")
        #    if codigo == busqueda:
        #        print(f"Codigo: {codigo}, Nombre: {nombre}, Categoria: {categoria}, Precio: {precio}, Fecha de registro: {fecha}")
        #        encontrado = True
        #        break 
            #print(linea.strip()) 
        #archivo.close() 
        #for i, producto in enumerate(productos, 1):
        #    if producto["nombre"].lower() == busqueda.lower():
        #        print(f"Codigo: {i}, Nombre: {producto['nombre'].capitalize()}, Categoria: {producto['categoria'].capitalize()}, Precio: {producto['precio']} Fecha de registro: {producto['fechaRegistro']}")
        #        encontrado = True
        #        break
        #if not encontrado:
        #    print("Producto no encontrado.")

    # ---------------- OPCIÓN 4: ELIMINAR ----------------
    elif opcion == "4":
        eliminar = input("Ingrese el ID del producto a eliminar: ")

        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM productos WHERE id = ?", (eliminar,))
        conexion.commit()

        if cursor.rowcount > 0:
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")

        conexion.close()

        #for i, producto in enumerate(productos, 1):
        #    if str(i) == eliminar:
        #        productos.pop(i-1)
        #        print("Producto eliminado exitosamente.")
        #        eliminado = True
        #        break
        # Leer todas las líneas
        #with open("datos.txt", "r") as archivo:
        #    lineas = archivo.readlines()

        # Abrir el archivo en modo escritura para reescribirlo
        #with open("datos.txt", "w") as archivo:
        #    for linea in lineas:
        #        codigo, nombre, categoria, precio, fecha = linea.strip().split(";")
        #        if codigo != eliminar:
        #            archivo.write(linea)
        #        else:
        #            eliminado = True
        #if not eliminado:
        #    print("Producto no encontrado.")
        #if eliminado:
        #    print("Producto eliminado exitosamente.")
        #else:
        #    print("Producto no encontrado.")

    # ---------------- OPCIÓN 5: SALIR ----------------
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")