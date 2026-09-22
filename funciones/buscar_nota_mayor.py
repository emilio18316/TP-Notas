def buscar_nota_mayor(notas):
    mayor = 0

    for nota in notas:
        if nota > mayor:
            mayor = nota

    return mayor
