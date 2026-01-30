from funciones import menu, notas, asistencias, informe

menu()

lista_alumnos = []

while True:
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")

    alumno = (nombre, apellido, edad)
    lista_alumnos.append(alumno)

    continuar = input("¿Quieres agregar otro alumno? (s/n): ").lower()
    if continuar != "s":
        break

print("\nAlumnos registrados:")
for alumno in lista_alumnos:
    print(alumno)

for alumno in lista_alumnos:
    nombre_completo = alumno[0] + " " + alumno[1]
    edad = int(alumno[2])

    print(f"\n--- Notas para {nombre_completo} ---")

    notas_alumno = notas()
    asistencia = asistencias()

    informe(nombre_completo, edad, notas_alumno, asistencia)
