matriz = []
# Outro opção seria criar a matriz sendo composta e puxar seu indice ao invés dos nomes
zero = []
um = []
dois = []

for c in range(0, 3):
    zero.append(int(input(f'Digite um valor para [0, {c}]: ')))

for c in range(0, 3):
    um.append(int(input(f'Digite um valor para [1, {c}]: ')))

for c in range(0, 3):
    dois.append(int(input(f'Digite um valor para [2, {c}]: ')))

matriz.append(zero)
matriz.append(um)
matriz.append(dois)
print('-=' * 30)
print(f'[ {matriz[0][0]:^5} ]', end='')
print(f'[ {matriz[0][1]:^5} ]', end='')
print(f'[ {matriz[0][2]:^5} ]')
print(f'[ {matriz[1][0]:^5} ]', end='')
print(f'[ {matriz[1][1]:^5} ]', end='')
print(f'[ {matriz[1][2]:^5} ]')
print(f'[ {matriz[2][0]:^5} ]', end='')
print(f'[ {matriz[2][1]:^5} ]', end='')
print(f'[ {matriz[2][2]:^5} ]')
