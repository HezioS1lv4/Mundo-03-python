'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])  # [:] cria uma copia
teste[0] = 'Maria'
teste[1] = 20
galera.append(teste[:])

print(galera[0])
print(galera[0][0])
print(galera[1][1])
print()
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''
   # print(p[0])

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
