#Combinations, Permutations e Product - ITERTOOLS
#Combinação - Ordem não importa - iterável + tamanho do grupo
#Permutação - Ordem importa
#Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['Joao', 'Joana', 'Luiz', 'Samira']

camisetas =[
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester']
]


# sem função print_iter
# print(*list(combinations(pessoas, 2)), sep='\n') 

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))