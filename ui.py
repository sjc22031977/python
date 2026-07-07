from colorama import Back, Fore, Style, init

init(autoreset=True)


def print_header() -> None:
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + "\n=== Sistema de Gestión Básica De Productos ===")


def print_menu() -> None:
    print(Fore.YELLOW + "\n1. Agregar producto")
    print(Fore.YELLOW + "2. Mostrar productos")
    print(Fore.YELLOW + "3. Buscar producto")
    print(Fore.YELLOW + "4. Eliminar producto")
    print(Fore.YELLOW + "5. Salir\n")


def prompt(text: str) -> str:
    return input(Fore.WHITE + text)


def print_error(message: str) -> None:
    print(Fore.RED + Style.BRIGHT + message)


def print_success(message: str) -> None:
    print(Fore.GREEN + message)


def print_section(title: str) -> None:
    print(Fore.MAGENTA + f"\n--- {title} ---")


def print_product(producto) -> None:
    print(Fore.WHITE + f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}, Fecha: {producto[6]}")
