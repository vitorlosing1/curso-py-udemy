import os
# criando arquivos com python
# funçao open para abrir um arquivo em python
# (ele pode ou nao existir)

# modos:
# r (leitura), w (escrita), x (para criacao)
# a (escreve ao final), b (binário)
# t (modo text), + (leitura e escrita)
# context manager - with (abre e fecha)

# métodos úteis
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline/lines

# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

# json.dump - gera arquivo json
# json.load - carrega arquivo json

caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# "+" dá função de escritura e leitura
# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end ='')
#     print(arquivo.readline().strip())

#     #READLINES
#     print('\nREADLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip()) 

# # 'a' não reseta o arquivo, 'w' e 'r' reseta
# # útil para arquivo de log
# with open(caminho_arquivo, 'a', encoding='utf8') as arquivo:
#     arquivo.write('Atenção\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

os.rename(caminho_arquivo, 'aula116.txt')