lista = []
numbers = int(input('Entre com um número ou digite -1 para parar: '))
while numbers != -1:
    lista.append(numbers)
    numbers = int(input('Entre com um número ou digite -1 para parar: '))

menor = min(lista)
lista.remove(menor)
segundo_menor = min(lista)

print('O segundo menor número da lista é:',segundo_menor)