def parametro(nro, crescente):
    for i in range(0, nro):
        if crescente:
            for j in range(1 , i + 2):
                print(j, end=" ")
        elif crescente == False:
            for j in range(i , 0, -1):
                print(j, end=" ")
        print()
nro = [1, 2, 3, 4, 5]
crescente = False
parametro(nro, crescente)