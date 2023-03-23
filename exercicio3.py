lista = []
numbers = int(input('Entre com um número ou digite -1 para parar: '))

while numbers != -1:
    lista.append(numbers)
    numbers = int(input('Entre com um número ou digite -1 para parar: '))

print('O maior elemento na lista é:',max(lista))
print('O menor elemento na lista é:',min(lista))