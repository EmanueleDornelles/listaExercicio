lista = []
number = int(input('Entre com um número ou digite -1 para parar: '))

while number != -1:
    lista.append(number)
    number = int(input('Entre com um número ou digite -1 para parar: '))

for i in lista:
    if i%2==0:
        print(i,end= " ")