lista = [[], []]
for n in range(1, 8):
    valor = int(input(f'Digite o {n}° valor: '))

    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 == 1:
        lista[1].append(valor)
# OU
# lista[0].sort()
# lista[1].sort()
print(f'Os valores pares foram: {sorted(lista[0])}')
print(f'Os valores ímpares foram: {sorted(lista[1])}')
