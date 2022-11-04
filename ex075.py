num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))
print(f'Você digitou os valores {num}')
print(f'Você digitou o numero 9, {num.count(9)} vezes.')
if 3 in num:
       print(f'O valor 3 apareceu na {num.index(3)}° posição.')
else:
       print('O numero 3 não foi digitado nenhuma vez.')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')
