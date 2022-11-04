listagem = ('mouse', 100,
            'teclado', 250,
            'fone', 300,
            'monitor', 1200,
            'computador', 2500)

print('-' * 40)
print(f'{"Loja Gamer H.S":^40} ')
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<31}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print(f'{"FIM":-^40}')
