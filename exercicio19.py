lista = []
numbers = int(input('Entre com um número ou digite -1 para parar: '))

while numbers != -1:
    if numbers%3==0:
        lista.append(numbers)
numbers = int(input('Entre com um número ou digite -1 para parar: '))

print('Os números divisíveis por 3 na lista são:',lista)