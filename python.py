from db import add_producto, delete_producto_by_id, fetch_all_productos, fetch_producto_by_id, init_db
from ui import print_error, print_header, print_menu, print_product, print_section, print_success, prompt


def main():
    init_db()

    while True:
        print_header()
        print_menu()
        opcion = prompt("Seleccione una opción: ")

        if opcion == "1":
            nombre = prompt("Nombre del producto: ")
            descripcion = prompt("Descripción del producto: ")
            try:
                cantidad = int(prompt("Cantidad del producto: "))
                precio = float(prompt("Precio del producto: "))
            except ValueError:
                print_error("ERROR! Cantidad debe ser un número entero y precio debe ser un número válido.")
                continue

            categoria = prompt("Categoría del producto: ")

            if precio < 0:
                print_error("ERROR! El precio no puede ser negativo.")
                continue

            precio = round(precio, 0)
            add_producto(nombre, descripcion, cantidad, precio, categoria)
            print_success("Producto agregado exitosamente.")

        elif opcion == "2":
            productos = fetch_all_productos()
            print_section("Productos Registrados")
            for producto in productos:
                print_product(producto)

        elif opcion == "3":
            try:
                busqueda = int(prompt("Ingrese el ID del producto a buscar: "))
            except ValueError:
                print_error("ERROR! El ID debe ser un número entero.")
                continue

            producto = fetch_producto_by_id(busqueda)
            if producto:
                print_section("Producto Encontrado")
                print_product(producto)
            else:
                print_error("Producto no encontrado.")

        elif opcion == "4":
            try:
                eliminar = int(prompt("Ingrese el ID del producto a eliminar: "))
            except ValueError:
                print_error("ERROR! El ID debe ser un número entero.")
                continue

            if delete_producto_by_id(eliminar):
                print_success("Producto eliminado exitosamente.")
            else:
                print_error("Producto no encontrado.")

        elif opcion == "5":
            print_success("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print_error("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    main()