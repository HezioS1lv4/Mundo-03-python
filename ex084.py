galera = list()
dado = list()
men = mai = tot = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    tot += 1
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'O total de pessoas cadastradas é {tot}')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for g in galera:
    if g[1] == mai:
        print(f'[{g[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for g in galera:
    if g[1] == men:
        print(f'[{g[0]}] ', end='')
print()
