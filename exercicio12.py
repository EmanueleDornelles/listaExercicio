lista = []
nomes = input('Entre com um nome ou digite -1 para parar: ')
while nomes != -1:
    if nomes in lista:
        print('O nome já existe na lista')
    break
else:
    lista.append(nomes)
nomes = input('Entre com um número ou digite -1 para parar: ')
print(lista)