# Ñ ESTÁ RESOLVIDO!!
# A matriz por algum motivo n fica lado a lado (3x3)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for lin in range(0, 3):
    for c in range(0, 3):
        matriz[lin][c] = int(input(f'Digite um valor para [{lin}, {c}]: '))
print('-=' * 30)
for lin in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[lin][c]:^5}]', end='')
        if matriz[lin][c] % 2 == 0:
            spar += matriz[lin][c]
        print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for lin in range(0, 3):
    scol += matriz[lin][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
   if c == 0:
       mai = matriz[1][c]
   elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior da segunda linha é {mai}.')
