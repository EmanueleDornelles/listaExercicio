numbers = int(input('Entre com um número ou digite -1 para parar: '))
soma_impar=[]
while numbers != -1:
    if numbers%2==1:
        soma_impar.append(numbers)
    numbers = int(input('Entre com um número ou digite -1 para parar: '))
  
print('A soma de numeros impares é',sum(soma_impar))