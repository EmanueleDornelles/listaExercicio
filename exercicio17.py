lista = []
nomes = input('Entre com uma lista de palavras separadas por virgula: ')
nomes = nomes.split(',')

for i in nomes:
    if 'e' in i.lower():
        lista.append(i)
print('As palavras com a letra "e" são: ',', '.join(lista))