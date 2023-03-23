lista = []
numbers = int(input('Entre com um número ou digite -1 para parar: '))
numeros_repetidos = []
while numbers != -1:
    if numbers in lista:
        numeros_repetidos.append(numbers)
    else:
        lista.append(numbers)
    numbers = int(input('Entre com um número ou digite -1 para parar: '))
print(sorted(lista))

