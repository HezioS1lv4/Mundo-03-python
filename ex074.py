from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# print(f'Os valores sorteados foram: {numeros}')
print(f'Os valores sorteados foram: ', end='')
for n in numeros:   # variavel que ira receber interação(n), variavel interada (numeros)
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')  # MAX e MIN, são funções da tupla que nos ajudam a descobrir o menor e o maior mais facilmente
print(f'O menor valor sorteado foi {min(numeros)}')
print(numeros)
