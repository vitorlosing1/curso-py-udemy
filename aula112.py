# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep = '\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 165.54},
    {'nome': 'Produto 2', 'preco': 17.23},
    {'nome': 'Produto 3', 'preco': 13.45},
    {'nome': 'Produto 4', 'preco': 15.80},
]

def filtrar_preco(produto):
    return produto ['preco'] > 100

# novos_produtos = [
#     p for p in produtos
#     if p ['preco'] > 10
# ]

novos_produtos = filter(
    # lambda p: p['preco'] > 100,
    filtrar_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)