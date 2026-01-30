import time
from colorama import init, Fore


def menu():
    init(autoreset=True)
    centro = "Luis Suñer"

    print(Fore.YELLOW + "====================================")
    time.sleep(0.5)
    print(Fore.CYAN + "Control de promoción de manuel")
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
        try:
            nombre = input(Fore.YELLOW + "Introduce un nombre válido: ")
            assert nombre.replace(" ", "").isalpha(), "El nombre solo puede contener letras"
            print(Fore.GREEN + "Nombre válido:", nombre)
            break
        except AssertionError as e:
            print(Fore.RED + str(e))

    
    while True:
        try:
            edad_input = input(Fore.YELLOW + "Dime tu edad (número válido): ")
            edad = int(edad_input)  # puede lanzar ValueError
            assert 0 < edad <= 120, "Edad fuera de rango"
            print(Fore.GREEN + "Edad válida")
            break
        except ValueError:
            print(Fore.RED + "Eso no es un número")
        except AssertionError as e:
            print(Fore.RED + str(e))

    return nombre, edad



def pedir_nota(texto):
    while True:
        try:
            nota_input = input(Fore.YELLOW + texto)
            nota = int(nota_input)  
            assert 0 <= nota <= 10, "Nota fuera de rango"
            print(Fore.GREEN + "Nota válida")
            return nota
        except ValueError:
            print(Fore.RED + "Eso no es un número")
        except AssertionError as e:
            print(Fore.RED + str(e))



def notas():
    n1 = pedir_nota("Dime tu primera nota: ")
    n2 = pedir_nota("Dime tu segunda nota: ")
    n3 = pedir_nota("Dime tu tercera nota: ")
    return n1, n2, n3



def asistencias():
    while True:
        try:
            asistencia_input = input(Fore.YELLOW + "Dime tus asistencias (%): ")
            asistencia = int(asistencia_input)
            assert 0 <= asistencia <= 100, "Asistencia fuera de rango"
            print(Fore.GREEN + "Asistencia válida")
            return asistencia
        except ValueError:
            print(Fore.RED + "Eso no es un número")
        except AssertionError as e:
            print(Fore.RED + str(e))



def informe(nombre, edad, notas, asistencia):
    n1, n2, n3 = notas
    media = (n1 + n2 + n3) / 3
    promociona = media >= 5 and asistencia >= 75

    tramo = "menor de edad" if edad <= 18 else "adulto"

    print(Fore.YELLOW + "=========================== INFORME FINAL ===================")
    print(f"Alumno: {nombre}")
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

