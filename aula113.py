from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 165.54},
    {'nome': 'Produto 2', 'preco': 17.23},
    {'nome': 'Produto 3', 'preco': 13.45},
    {'nome': 'Produto 4', 'preco': 15.80},
]

# def funcao_reduce(acumulador, produto):
#     print(acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']

# total = reduce (

#     funcao_reduce,
#     produtos,
#     0
# )
total = reduce (

    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print('total é', total)

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))