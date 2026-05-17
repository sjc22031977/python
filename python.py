# nombre = input("Introduce su nombre: ") 
# apellido = input("Introduce tu apellido: ")
# edad = int(input("Introduce su edad: "))
# email = input("Introduce su correo electrónico: ")
# total = 0
# if nombre == "" or apellido == "" or edad < 1 or email == "" or email.count("@") != 1:
#     print("ERROR!")
# else:
#     print("Nombre: ", nombre.title())
#     print("Apellido: ", apellido.title())
#     print("Edad: ", edad, "años")
#     print("Correo electrónico: ", email.strip())
#     if edad < 13: 
#         print("Sos menor a trece años.")
#     elif edad < 18: 
#         print("Sos un o una adolescente.")
#     elif edad < 60: 
#         print("Sos una persona adulta.")
#     else: 
#         print("Sos una persona adulta mayor.")

# for i in range(0, 6):
#     ingreso = int(input("Introduce sus ingresos del ultimo mes: "))
#     total += ingreso
#     if ingreso <= 0:
#         print("ERROR!")
#         ingreso = int(input("Introduce sus ingresos del ultimo mes: "))
#         total += ingreso
#     else:
#         print("Ingresos: ", ingreso, "pesos")

# print("Total de ingresos: ", total, "pesos")
# print("Promedio mensual: ", total / 6, "pesos")
# clientes = []
# for i in range(0, 6):
#     cliente = input("Introduce el nombre del cliente: ")
#     if cliente == "":
#         print("Cliente", i+1, ": [ALERTA] Nombre no válido ")
#         cliente = input("Introduce el nombre del cliente: ")
#     else:
#         print("Cliente", i+1, ": ", cliente.title())
#         clientes.append(cliente.title())

# i = 0 
# while i < len(clientes): 
#     print("Cliente", i+1, ": ", clientes[i].capitalize()) 
# nombre = input("Introduce su nombre: ") 
# apellido = input("Introduce tu apellido: ")
# edad = int(input("Introduce su edad: "))
# email = input("Introduce su correo electrónico: ")
# total = 0
# if nombre == "" or apellido == "" or edad < 1 or email == "" or email.count("@") != 1:
#     print("ERROR!")
# else:
#     print("Nombre: ", nombre.title())
#     print("Apellido: ", apellido.title())
#     print("Edad: ", edad, "años")
#     print("Correo electrónico: ", email.strip())
#     if edad < 13: 
#         print("Sos menor a trece años.")
#     elif edad < 18: 
#         print("Sos un o una adolescente.")
#     elif edad < 60: 
#         print("Sos una persona adulta.")
#     else: 
#         print("Sos una persona adulta mayor.")

# for i in range(0, 6):
#     ingreso = int(input("Introduce sus ingresos del ultimo mes: "))
#     total += ingreso
#     if ingreso <= 0:
#         print("ERROR!")
#         ingreso = int(input("Introduce sus ingresos del ultimo mes: "))
#         total += ingreso
#     else:
#         print("Ingresos: ", ingreso, "pesos")

# print("Total de ingresos: ", total, "pesos")
# print("Promedio mensual: ", total / 6, "pesos")
# clientes = []
# for i in range(0, 6):
#     cliente = input("Introduce el nombre del cliente: ")
#     if cliente == "":
#         print("Cliente", i+1, ": [ALERTA] Nombre no válido ")
#         cliente = input("Introduce el nombre del cliente: ")
#     else:
#         print("Cliente", i+1, ": ", cliente.title())
#         clientes.append(cliente.title())

# i = 0 
# while i < len(clientes): 
#     print("Cliente", i+1, ": ", clientes[i].capitalize()) 
#     i += 1 

clientes = []
while True:
    nombre = input("Introduce su nombre: (Para salir, escriba 'Fin') ")
    if nombre == "Fin":
        print("Programa finalizado.")
        break
    elif nombre == "":
        print("ERROR!")
        nombre = input("Introduce su nombre: ")
    else:
        clientes.append(nombre.title())

for i in clientes:
    print("Cliente: ", i.capitalize())
