tabela = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', ' Atletico-PR', 'Atlético-MG',
          'São Paulo', 'América-MG', 'Fortaleza', 'Botafogo', 'Santos', 'Bragantino', 'Goiás', 'Coritiba', 'Cuiabá',
           'Ceará-SC', 'Atlético-GO', 'Avaí', 'Juventude')

# deixar um embaixo do outro
# for t in tabela:
#    print(t)

# print(tabela)
'''for ordem in range(0, len(tabela[5])):
    print(f'O {tabela} está em {ordem}°')
'''
print(f'Os 5 primeiros colocados ta tabela são {tabela [:5]}')
print(f'Os ultimos 4 colocados são {tabela [-4:]}')
print(f'Os times em ordem alfabética: {sorted(tabela)}')
print(f'Em que posição se encontra o Flamengo? {tabela.index("Flamengo")}')
