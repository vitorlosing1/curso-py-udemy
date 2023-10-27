#Problema dos parâmetros mutáveis em funções Python

# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

# lista1 = []
# cliente1 = adiciona_clientes('Luiz', lista1)
# adiciona_clientes('Joana', cliente1)
# print(cliente1)

# cliente2 = adiciona_clientes('Maria')
# adiciona_clientes('Jorge', cliente2)
# print(cliente2)


# FORMA IDEAL PARA PARAMETROS MUTÁVEIS
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('João', cliente1)
cliente1.append('Mario')
print(cliente1)

cliente2 = adiciona_clientes('Maria')
adiciona_clientes('Jorge', cliente2)
print(cliente2)

cliente3 = adiciona_clientes('Marcio')
adiciona_clientes('Viviane', cliente3)
print(cliente3)