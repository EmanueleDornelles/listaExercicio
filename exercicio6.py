lista = []
numbers = int(input('Entre com um número ou digite -1 para parar: '))

while numbers != -1:
    lista.append(numbers)
    numbers = int(input('Entre com um número ou digite -1 para parar: '))

print(sorted(lista,reverse = True))