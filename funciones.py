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



def informacion():
    
    while True:
        nombre = input(Fore.YELLOW + "Introduce tu nombre: ")
        if nombre.replace(" ", "").isalpha():
            print(Fore.GREEN + "Nombre válido")
            break
        else:
            print(Fore.RED + "El nombre solo puede tener letras")

    
    while True:
        apellidos = input(Fore.YELLOW + "Introduce tus apellidos: ")
        if apellidos.replace(" ", "").isalpha():
            print(Fore.GREEN + "Apellidos válidos")
            break
        else:
            print(Fore.RED + "Los apellidos solo pueden tener letras")

    
    while True:
        try:
            edad = int(input(Fore.YELLOW + "Dime tu edad: "))
            if 0 < edad <= 120:
                print(Fore.GREEN + "Edad válida")
                break
            else:
                print(Fore.RED + "Edad fuera de rango")
        except:
                print(Fore.RED + "Eso no es un número")

    return nombre, apellidos, edad



def pedir_nota(texto):
    while True:
        try:
            nota = int(input(Fore.YELLOW + texto))
            if 0 <= nota <= 10:
                print(Fore.GREEN + "Nota válida")
                return nota
            else:
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
                print(Fore.GREEN + "Asistencia válida")
                return asistencia
            else:
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
        print(Fore.GREEN + "✅ Promociona: Sí")
        print(Fore.GREEN + "Felicidades")
    else:
        print(Fore.RED + "❌ Promociona: No")
        print(Fore.YELLOW + "Ánimo")

        print(Fore.YELLOW + "=============================================================")
