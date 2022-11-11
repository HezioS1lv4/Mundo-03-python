lista = list()

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
    elif n > lista[len(lista) - 1]:   # Pegar o ultimo valor
        lista.append(n)
        print('Add ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
