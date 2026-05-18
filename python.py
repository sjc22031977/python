# clientes = []
# while True:
#     nombre = input("Introduce su nombre: (Para salir, escriba 'Fin') ")
#     if nombre == "Fin":
#         print("Programa finalizado.")
#         break
#     elif nombre == "":
#         print("ERROR!")
#         nombre = input("Introduce su nombre: ")
#     else:
#         clientes.append(nombre.title())

# clientes.sort()
# print("\nClientes ordenados:")
# for i in clientes:
#     print("Cliente:", i.capitalize())

# # Creamos una lista vacía para almacenar los diccionarios 
# productos = [] 
# # Bucle para ingresar los datos de varios productos
# while True: 
#     print("\nIngresá los datos del producto.[vacío para finalizar]:") 
#     nombre = input("Nombre del producto: ") 

#     # Condición para salir del bucle si el nombre está vacío 
#     if nombre == "": 
#         break

#     precio = float(input("Precio del producto: "))

#     # Creamos un diccionario con los datos ingresados 
#     producto = { 
#         "nombre": nombre, 
#         "precio": precio 
#     } 
   
#     # Agregamos el diccionario a la lista de productos 
#     productos.append(producto) 
 
# # Mostramos los datos de todos los productos registrados 
# print("\n--- Productos Registrados ---") 
# for producto in productos: 
#    print(f"Nombre: {producto['nombre'].capitalize()}, Precio: {producto['precio']}") 

productos = []
while True:
    print("\nSistema de Gestión Básica De Productos")
    print("\n1. Agregar producto")
    print("\n2. Mostrar productos")
    print("\n3. Buscar producto")
    print("\n4. Eliminar producto")
    print("\n5. Salir")
    print("\n")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría del producto: ")
        precio = float(input("Precio del producto: "))
        if precio < 0:
            print("ERROR! El precio no puede ser negativo.")
            continue
        precio = round(precio, 0)
        producto = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }
        productos.append(producto)
        print("Producto agregado exitosamente.")
    elif opcion == "2":
        print("\n--- Productos Registrados ---")
        for producto in productos:
            print(f"Nombre: {producto['nombre'].capitalize()}, Precio: {producto['precio']}")
    elif opcion == "3":
        busqueda = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for producto in productos:
            if producto["nombre"].lower() == busqueda.lower():
                print(f"Producto encontrado: Nombre: {producto['nombre'].capitalize()}, Precio: {producto['precio']}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "4":
        eliminar = input("Ingrese el nombre del producto a eliminar: ")
        eliminado = False
        for producto in productos:
            if producto["nombre"].lower() == eliminar.lower():
                productos.remove(producto)
                print("Producto eliminado exitosamente.")
                eliminado = True
                break
        if not eliminado:
            print("Producto no encontrado.")
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")