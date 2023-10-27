# def zipper(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i],lista2[i]) for i in range(intervalo)
#     ]

# lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista2 = ['BA', 'SP', 'MG', 'RJ']
# print(zipper(lista1, lista2))

from itertools import zip_longest

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(lista1, lista2)))

print(list(zip_longest(lista1, lista2, fillvalue='sem cidade')))