from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Vitor', 'nota': 'C'},
    {'nome': 'Jorge', 'nota': 'D'},
    {'nome': 'Sabrina', 'nota': 'A'},
    {'nome': 'Rodolfo', 'nota': 'D'},
    {'nome': 'Barbara', 'nota': 'B'},
    {'nome': 'Samanta', 'nota': 'A'},
    {'nome': 'Laís', 'nota': 'C'},
]

def ordena(aluno):
    return aluno ['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)