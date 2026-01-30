from funciones import menu, notas, asistencias, informe

menu()

lista_alumnos = []

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje)
        if texto.replace(" ", "").isalpha():
            return texto
        print("Solo se permiten letras")

def pedir_edad():
    while True:
        try:
            edad = int(input("Edad: "))
            if 0 < edad <= 120:
                return edad
            print("Edad fuera de rango")
        except:
            print("Eso no es un número")


# Registrar alumnos
while True:
    nombre = pedir_texto("Nombre: ")
    apellido = pedir_texto("Apellido: ")
    edad = pedir_edad()

    print(f"\n--- Notas para {nombre} {apellido} ---")
    notas_alumno = notas()
    asistencia = asistencias()

    lista_alumnos.append({
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "notas": notas_alumno,
        "asistencia": asistencia
    })

    if input("¿Quieres agregar otro alumno? (s/n): ").lower() != "s":
        break


# MENÚ PARA CONSULTAR INFORMES
while True:
    print("\n=== CONSULTAR INFORMES ===")
    print("1. Ver informe de un alumno")
    print("2. Ver informes de todos")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre_buscar = input("Nombre del alumno a buscar: ").lower()

        encontrado = False
        for alumno in lista_alumnos:
            if alumno["nombre"].lower() == nombre_buscar:
                informe(
                    alumno["nombre"],
                    alumno["apellido"],
                    alumno["edad"],
                    alumno["notas"],
                    alumno["asistencia"]
                )
                encontrado = True
                break

        if not encontrado:
            print("Alumno no encontrado")

    elif opcion == "2":
        for alumno in lista_alumnos:
            informe(
                alumno["nombre"],
                alumno["apellido"],
                alumno["edad"],
                alumno["notas"],
                alumno["asistencia"]
            )

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")
