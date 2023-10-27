#POSITIONAL-ONLY-PARAMETERS E KEYWORD-ONLY-ARGUMENTS
# Tudo antes da / deve ser posicional
# E tudo após * deve ser nomeado

def soma (a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)

soma(1, 2, c=3, nome='teste')