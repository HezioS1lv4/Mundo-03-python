from random import randint
from time import sleep
from operator import itemgetter
# Guanabara solução
jogo = {'jogador01': randint(1, 7),
        'jogador02': randint(1, 7),
        'jogador03': randint(1, 7),
        'jogador04': randint(1, 7),}

ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('   == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}.')

# /////////////////////////////// #

'''jogadores = dict()
jogadores['jogador01'] = randint(1, 7)
jogadores['jogador02'] = randint(1, 7)
jogadores['jogador03'] = randint(1, 7)
jogadores['jogador04'] = randint(1, 7)

print('Valores sorteados: ')
sleep(1)
print(f'    O jogador01 tirou {jogadores["jogador01"]}')
sleep(1)
print(f'    O jogador02 tirou {jogadores["jogador02"]}')
sleep(1)
print(f'    O jogador03 tirou {jogadores["jogador03"]}')
sleep(1)
print(f'    O jogador04 tirou {jogadores["jogador04"]}')

maior = menor = jogadores['jogador01']

if jogadores['jogador02'] > jogadores['jogador01']:
    maior = jogadores['jogador02']
if jogadores['jogador03'] > jogadores['jogador02']:
    maior = jogadores['jogador03']
if jogadores['jogador04'] > jogadores['jogador03']:
    maior = jogadores['jogador04']

print('Ranking dos jogadores: ')
print(maior)
'''
