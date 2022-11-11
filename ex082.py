lista = list()
p = list()
impar = []

while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        p.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=' * 30)
print(f'A lista normal é {lista}')
print(f'A lista de pares é {p}')
print(f'A lista de impares é {impar}')
