from itertools import zip_longest

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

lista_soma2 = [x + y for x, y in zip_longest(lista_a, lista_b,
 fillvalue= 0)]
print(lista_soma2)

