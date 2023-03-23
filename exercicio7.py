lista = []
palavras = input('Entre com uma lista de nomes separadas por virgula: ')
palavras = palavras.split(',')
for i in palavras:
    lista.append(i)
print('O maior nome na lista é:',max(lista))
print('O menor nome na lista é:',min(lista))