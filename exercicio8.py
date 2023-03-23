lista = []
numbers = int(input('Entre com um número ou digite -1 para parar: '))
maior_10=[]
while numbers != -1:
    lista.append(numbers)
    numbers = int(input('Entre com um número ou digite -1 para parar: '))
    if numbers>10:
        maior_10.append(numbers)
print(maior_10)
