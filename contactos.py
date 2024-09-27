# Diccionario para almacenar los contactos
agenda = {}

# Función para agregar un contacto a la agenda
def agregar_contacto():
    # Solicita el nombre del contacto
    nombre = input("Ingrese el nombre: ")
    # Solicita el número de teléfono del contacto
    telefono = input("Ingrese el teléfono: ")
    # Agrega el contacto al diccionario 'agenda'
    agenda[nombre] = telefono

# Función para mostrar todos los contactos de la agenda
def mostrar_contactos():
    print("Contactos:")
    # Itera sobre los elementos del diccionario para mostrar los contactos
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")

# Función para buscar un contacto por su nombre
def buscar_contacto():
    # Solicita el nombre del contacto a buscar
    nombre = input("Ingrese el nombre a buscar: ")
    # Verifica si el contacto existe en la agenda
    if nombre in agenda:
        # Muestra el teléfono del contacto si se encuentra
        print(f"Teléfono: {agenda[nombre]}")
    else:
        # Muestra un mensaje si el contacto no está en la agenda
        print("Contacto no encontrado")

# Bucle principal del programa
while True:
    # Muestra el menú de opciones
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Salir")
    
    # Solicita al usuario que elija una opción
    opcion = input("Ingrese la opción: ")

    # Llama a la función correspondiente según la opción seleccionada
    if opcion == "1":
        agregar_contacto()  # Llama a la función para agregar un contacto
    elif opcion == "2":
        mostrar_contactos()  # Llama a la función para mostrar todos los contactos
    elif opcion == "3":
        buscar_contacto()  # Llama a la función para buscar un contacto
    elif opcion == "4":
        # Rompe el bucle y termina el programa
        break
    else:
        # Muestra un mensaje si la opción no es válida
        print("Opción inválida")
