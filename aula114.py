# função recursiva podem se chamar de volta
# divide problemas maiores em menores

# def recursiva (inicio=0, fim=10):

#     print(inicio, fim)

#     #caso base
#     if inicio >= fim:
#         return fim
    
#     #caso recursivo
#     #conta até chegar no final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva(0, 1000))

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
 