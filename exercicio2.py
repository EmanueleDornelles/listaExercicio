lista = []
palavras = input('Entre com uma lista de palavras separadas por virgula: ')
palavras = palavras.split(',')

for i in palavras:
    if i.lower().startswith('a'):
        lista.append(i)
print('As palavras com a letra são: ',', '.join(lista))