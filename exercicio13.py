lista = []
numbers = int(input('Entre com um número ou digite -1 para parar: '))
while numbers != -1:
    lista.append(numbers)
    numbers = int(input('Entre com um número ou digite -1 para parar: '))

maior = max(lista)
lista.remove(maior)
segundo_maior = max(lista)

print('O segundo maior número da lista é:',segundo_maior)
