import time
from colorama import init, Fore

def menu():
    init(autoreset=True)
    centro = "Luis Suñer"

    print(Fore.YELLOW + "====================================")
    time.sleep(0.5)
    print(Fore.CYAN + "Control de promoción de Manuel")
    time.sleep(0.5)
    print(Fore.YELLOW + "====================================")
    time.sleep(0.5)
    print(Fore.YELLOW + "Cargando...")
    print(Fore.YELLOW + "====================================")
    time.sleep(0.3)
    print(Fore.YELLOW + "(˵ ͡° ͜ʖ ͡°˵)" + Fore.GREEN + "==============100%======================")
    print(Fore.YELLOW + "Hola " + centro)
    print(Fore.YELLOW + "====================================")
    time.sleep(0.5)


# -------------------------
# TUS FUNCIONES ORIGINALES
# -------------------------

def informacion():
    while True:
        nombre = input(Fore.YELLOW + "Introduce tu nombre: ")
        if nombre.replace(" ", "").isalpha():
            break
        print(Fore.RED + "El nombre solo puede tener letras")

    while True:
        apellidos = input(Fore.YELLOW + "Introduce tus apellidos: ")
        if apellidos.replace(" ", "").isalpha():
            break
        print(Fore.RED + "Los apellidos solo pueden tener letras")

    while True:
        try:
            edad = int(input(Fore.YELLOW + "Dime tu edad: "))
            if 0 < edad <= 120:
                break
            print(Fore.RED + "Edad fuera de rango")
        except:
            print(Fore.RED + "Eso no es un número")

    return nombre, apellidos, edad


def pedir_nota(texto):
    while True:
        try:
            nota = int(input(Fore.YELLOW + texto))
            if 0 <= nota <= 10:
                return nota
            print(Fore.RED + "La nota debe estar entre 0 y 10")
        except:
            print(Fore.RED + "Eso no es un número")


def notas():
    n1 = pedir_nota("Dime tu primera nota: ")
    n2 = pedir_nota("Dime tu segunda nota: ")
    n3 = pedir_nota("Dime tu tercera nota: ")
    return n1, n2, n3


def asistencias():
    while True:
        try:
            asistencia = int(input(Fore.YELLOW + "Dime tus asistencias (%): "))
            if 0 <= asistencia <= 100:
                return asistencia
            print(Fore.RED + "Debe ser entre 0 y 100")
        except:
            print(Fore.RED + "Eso no es un número")


def informe(nombre, apellidos, edad, notas, asistencia):
    n1, n2, n3 = notas
    media = (n1 + n2 + n3) / 3
    promociona = media >= 5 and asistencia >= 75
    tramo = "menor de edad" if edad <= 18 else "adulto"

    print(Fore.YELLOW + "=========================== INFORME FINAL ===================")
    print(f"Alumno: {nombre} {apellidos}")
    print(f"Edad: {edad} -> {tramo}")
    print(f"Notas: {n1}, {n2}, {n3} | Media: {media:.2f}")
    print(f"Asistencia: {asistencia}%")

    if promociona:
        print(Fore.GREEN + "Promociona: Sí")
    else:
        print(Fore.RED + "Promociona: No")

    print(Fore.YELLOW + "=============================================================")


# -------------------------
# AQUÍ VA TODO TU MAIN ORIGINAL
# -------------------------

def app():

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

    # -------- REGISTRO DE ALUMNOS --------
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

    # -------- CONSULTAR INFORMES --------
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
