lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    saida = str(input('Deseja continuar? [S/N]')).upper().strip()

    while saida not in 'SN':
        saida = str(input('Digite uma opção válida! [S/N]')).upper().strip()
    if saida == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente: {lista}')

if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor ñ está na lista!')
print('FIM!')
