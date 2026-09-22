def notas_impares(notas):
    impares = list()

    for nota in notas:
        if nota % 2 != 0:
            impares.append(nota)

    return impares
