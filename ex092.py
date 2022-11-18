from datetime import date
infos = dict()

infos['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
data = date.today().year
infos['idade'] = data - nascimento
infos['ctps'] = int(input('CTPS: '))

if infos['ctps'] == 0:
    print('Você ñ tem carteira de trabalho!')
    infos['anoContrat'] = 0
if infos['ctps'] != 0:
    print('-=-= Informações da ctps -=-=')
    infos['anoContrat'] = int(input('   Ano de contratação: '))
    infos['salario'] = float(input('    Salário: R$'))

diferenca = (infos["anoContrat"] + 35) - data
print(f'Você tem {infos["idade"]} anos e falta {diferenca} anos para se aposentar.')
