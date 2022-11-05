# Variáveis Compostas -> [listas]

'''
num = [2, 5, 9, 1]
num[2] = 22  # substituir valor
num.append(8)  # add valor na última posição
num.sort(reverse=True)   # ao contrário -> (reverse=True)
num.insert(2, 2)  # na posição 2, ele ira inserir 0
# num.pop()  # deleta o ultimo elemento
# num.pop(2)  # deleta o elemento de posição 2
num.remove(2)  # começa da 1° posição e deleta o primeiro valor (2) encontrado
if 4 in num:
    num.remove(4)
else:
    print('Nenhum valor encontrado.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
'''

'''
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')
'''

a = [2, 3, 4, 7]
# b = a  #// ele cria uma ligação entre os 2 em que n se pode modificar somente o b
b = a[:]  # b recebe todos os valores de a, ou seja, tenho liberdade para modificar
b[2] = 8
print(a)
print(b)
