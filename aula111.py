from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep ='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 165.54},
    {'nome': 'Produto 2', 'preco': 17.23},
    {'nome': 'Produto 3', 'preco': 13.45},
    {'nome': 'Produto 4', 'preco': 15.80},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial (
    aumentar_porcentagem,
    porcentagem = 1.1
)

# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return {
        **produto,
         'preco': aumentar_dez_porcento(
        produto['preco'])
    }


novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))

print_iter(produtos)
print_iter(novos_produtos)