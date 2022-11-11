lista = []
while True:
    n = int((input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Add com sucesso...')
    else:
        print('Valor duplicado. ñ será considerado!')
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break

print('-=' * 30)
lista.sort()
print(f'Você digitou os valores {lista} ')

'''lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    saida = str(input('Deseja continuar? [S/N]')).upper().strip()

#    for v in lista:
#        if v == v:
#            igual = v == v
#            lista.remove(igual)

    while saida not in 'SN':
        saida = str(input('Digite uma opção válida! [S/N]')).upper().strip()
    if saida == 'N':
        break
print(f'Os valores foram {lista}')
print(f'Os valores em ordem crescente: {sorted(lista)}')
print('FIM!')
'''