'''pessoas = {'nome': 'Hézio', 'sexo': 'M', 'idade': '19'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.items())
# print(pessoas.values())

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

# del pessoas['sexo']
pessoas['peso'] = 78.9  # add item ao dict
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''

'''brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
'''

estado = dict()
brasil = list()

for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla de Estado: '))
    brasil.append(estado.copy())
# print(brasil)

for e in brasil:
    print(e)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
