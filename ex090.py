informacoes = dict()

informacoes['nome'] = str(input('Nome: '))
informacoes['media'] = float(input(f'Média de {informacoes["nome"]}: '))
if informacoes['media'] < 7:
    informacoes['situacao'] = 'Reprovado'
else:
    informacoes['situacao'] = 'Aprovado'

print(f'Nome é igual a {informacoes["nome"]}')
print(f'Média é igual a {informacoes["media"]}')
print(f'Situação é igual a {informacoes["situacao"]}')

# OU
for k, v in informacoes.items():
    print(f'{k} é igual a {v}')
