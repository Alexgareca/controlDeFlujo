numeroInicial = int(input('Ingrese el numero inicial: '))
numeroFinal = int(input('Ingrese el numero final: '))
lista = []
while numeroInicial <= numeroFinal:
    if (numeroInicial % 2) != 0:
        lista.append(numeroInicial)
    numeroInicial += 1

print(lista)

