# Variaveis compostas -> {Tuplas}, Listas, Dicionarios

# As tuplas são IMUTÁVEIS, ou seja, n consegue mudar o que foi definido

lanche = ('Hambúrguer', 'Suco', 'pizza', 'Pudim', 'Batata Frita')

# fatiamento
'''print(lanche)
print(lanche[2])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:]) # Começa no -2 e vai até o final, sentido Direita
'''
#///////////////////////////////////#

'''#for comida in lanche:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')  # na posição {cont}
print('Caramba! Comi muito')
# OU
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')
print('Comi pra caramba!')
'''

# print(sorted(lanche))  # O sorted coloca em ordem os elementos, mas nao altera os mesmos
# print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
# print(c)
# print(len(c))
# print(c.count(2))
# print(c.index(8))
# print(c.index(5, 1))  # ele ira começar pelo indice 1

pessoa = ('Hézio', 19, 'M', 1.89)
del(pessoa)  # deleta uma variavel da memória
print(pessoa)
