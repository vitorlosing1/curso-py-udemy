import json

pessoa = {
    'nome': 'Vitor',
    'sobrenome': 'Lurici de Moraes',
    'enderecos': [
        {'rua': 'R1', 'numero': 325},
        {'rua': 'R2', 'numero': 13},
    ],
    'altura': 1.8,
    'dev': True,
}

with open('aula117.json', 'w', encoding ='utf8') as arquivo:
    json.dump(pessoa, arquivo, indent=2)


with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))

    print(pessoa['nome'])

