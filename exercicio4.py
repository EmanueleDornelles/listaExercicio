lista = []
numbers = int(input('Entre com um número ou digite -1 para parar: '))

while numbers != -1:
    lista.append(numbers)
    numbers = int(input('Entre com um número ou digite -1 para parar: '))

print('A média entre os números é:',sum(lista)/len(lista))