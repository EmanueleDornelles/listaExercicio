lista = []
numbers = int(input('Entre com um número ou digite -1 para parar: '))
menor_5=[]
while numbers != -1:
    lista.append(numbers)
    numbers = int(input('Entre com um número ou digite -1 para parar: '))
    if numbers<5 and numbers != -1:
        menor_5.append(numbers)
print(menor_5)