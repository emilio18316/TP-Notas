from funciones.ver_notas import ver_notas
from funciones.calcular_promedio import calcular_promedio
from funciones.buscar_nota_mayor import buscar_nota_mayor
from funciones.calcular_media import calcular_media
from funciones.notas_impares import notas_impares

notas = list()
opcion = 0

while opcion != 7:
    print("\n=== SISTEMA DE GESTIÓN DE NOTAS ===")
    print("1. Agregar nota")
    print("2. Ver notas")
    print("3. Calcular promedio")
    print("4. Buscar nota mayor")
    print("5. Calcular media")
    print("6. Ver solamente notas impares")
    print("7. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        nota = int(input("Ingrese una nota: "))
        notas.append(nota)
    elif opcion == 2:
        ver_notas(notas)
    elif opcion == 3:
        print("Promedio:", calcular_promedio(notas))
    elif opcion == 4:
        print("Nota mayor:", buscar_nota_mayor(notas))
    elif opcion == 5:
        print("Media:", calcular_media(notas))
    elif opcion == 6:
        ver_notas(notas_impares(notas))
    elif opcion == 7:
        print("Fin")
    else:
        print("Opción incorrecta")
