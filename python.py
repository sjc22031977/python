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
        productos.sort(key=lambda x: x["nombre"])
        for i, producto in enumerate(productos, 1):
            print(f"Codigo: {i}, Nombre: {producto['nombre'].capitalize()}, Categoria: {producto['categoria'].capitalize()}, Precio: {producto['precio']}")
    elif opcion == "3":
        busqueda = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for i, producto in enumerate(productos, 1):
            if producto["nombre"].lower() == busqueda.lower():
                print(f"Codigo: {i}, Nombre: {producto['nombre'].capitalize()}, Categoria: {producto['categoria'].capitalize()}, Precio: {producto['precio']}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "4":
        eliminar = input("Ingrese el código del producto a eliminar: ")
        eliminado = False
        for i, producto in enumerate(productos, 1):
            if str(i) == eliminar:
                productos.pop(i-1)
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