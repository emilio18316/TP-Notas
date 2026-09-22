def calcular_promedio(notas):
    if len(notas) == 0:
        return 0

    total = 0

    for nota in notas:
        total = total + nota

    return total / len(notas)
