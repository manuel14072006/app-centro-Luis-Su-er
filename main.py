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



while True:
    nombre = pedir_texto("Nombre: ")
    apellido = pedir_texto("Apellido: ")
    edad = pedir_edad()

    lista_alumnos.append((nombre, apellido, edad))

    if input("¿Quieres agregar otro alumno? (s/n): ").lower() != "s":
        break



print("\nAlumnos registrados:")
for nombre, apellido, edad in lista_alumnos:
    print(f"{nombre} {apellido} - {edad} años")

    

for nombre, apellido, edad in lista_alumnos:
    print(f"\n--- Notas para {nombre} {apellido} ---")

    notas_alumno = notas()
    asistencia = asistencias()

    informe(nombre, apellido, edad, notas_alumno, asistencia)
