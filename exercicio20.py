lista = []
palavras = input('Entre com uma lista de palavras separadas por espaço: ').split()

for i in palavras:
    if len(i)%2!=0:
        lista.append(i)
print('As palavras impares são: ',lista)