from random import sample

def busqueda (a,coordenadass):
    cont = 0
    for xd in coordenadass:
        if a != xd :
            cont = cont+1
        else:
            return(cont)
    


print("Memocrice")
n = int(input("Cuantas cartas desea jugar: "))

while n <= 1 :
    n = int(input("Escoja otro numero: "))

cartas = list(range(1,n+1))
cartas2 = list(range(1,n+1))

lista = cartas + cartas2
lista = sample(lista,k=(2*n))

coordenadas = []
estados = []

n2 = n*2

for est in range(0,n2):
    estados.append("*")

for fila in range(1,3):
        for columna in range(1,1+n):
            coord = (fila,columna)
            coordenadas.append(coord)

puntos1 = 0
puntos2 = 0
cont = 0


while (puntos1 + puntos2) < n :
    print("\n")
    print("puntos jugador 1:")
    print(puntos1)
    print("puntos jugador 2:")
    print(puntos2)
    print("\n")

    c1 = []
    c2 = []
    contnum = 0 
    for x in coordenadas:
        if x[0] == 1:
            if estados[contnum] == "*":
                c1.append(x)
            else:
                c1.append("--")
        else:
            if estados[contnum] == "*":
                c2.append(x)
            else:
                c2.append("--")
    print(c1)
    print(c2)


    if cont == 0:
        print("Jugador 1 primera carta: ")
        ff = int(input("fila: "))
        cc = int(input("columna: "))

        coord1 = (ff,cc)
        index1 = busqueda(coord1, coordenadas)
        indexcol = coord1[1]-1
        numcard = lista[index1]
        if coord1[0] == 1:
            c1[indexcol] = numcard
        else:
            c2[indexcol] = numcard
        
        print(c1)
        print(c2)

        print("Jugador 1 segunda carta: ")
        ff2 = int(input("fila: "))
        cc2 = int(input("columna: "))

        coord2 = (ff2,cc2)
        index2 = busqueda(coord2, coordenadas)
        indexcol2 = coord2[1]-1
        numcard2 = lista[index2]
        if coord2[0] == 1:
            c1[indexcol2] = numcard2
        else:
            c2[indexcol2] = numcard2

        print(c1)
        print(c2)

        if numcard2 == numcard:
            estados[index1] = "--"
            estados[index2] = "--"
            puntos1 = puntos1+1

        cont = 1


    elif cont == 1:
        print("Jugador 2 primera carta: ")
        ff = int(input("fila: "))
        cc = int(input("columna: "))

        coord1 = (ff,cc)
        index1 = busqueda(coord1, coordenadas)
        indexcol = coord1[1]-1
        numcard = lista[index1]
        if coord1[0] == 1:
            c1[indexcol] = numcard
        else:
            c2[indexcol] = numcard
        
        print(c1)
        print(c2)

        print("Jugador 2 segunda carta: ")
        ff2 = int(input("fila: "))
        cc2 = int(input("columna: "))

        coord2 = (ff2,cc2)
        index2 = busqueda(coord2, coordenadas)
        indexcol2 = coord2[1]-1
        numcard2 = lista[index2]
        if coord2[0] == 1:
            c1[indexcol2] = numcard2
        else:
            c2[indexcol2] = numcard2

        print(c1)
        print(c2)

        if numcard2 == numcard:
            estados[index1] = "--"
            estados[index2] = "--"
            puntos2 = puntos2+1
        
        cont = 0


if puntos1 < puntos2:
    print("Jugador 2 gana!")
elif puntos1 > puntos2:
    print("Jugador 1 gana!")
else:
    print("Empate :(")


print(lista)

