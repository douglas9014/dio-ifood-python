print()

curso = "cUrSo dE pYThoN"
print('Tudo em maiúsculo:', curso.upper())
print('Tudo em minúsculo:', curso.lower())
print('Primeiras letras das palavras em maiúsculo:', curso.title())
print()

curso = "     Python  "
print('Remove espaços em branco...')
print('...dos dois lados:', curso.strip() + "!")
print('...à esquerda:', curso.lstrip() + "!")
print('...à direita:', curso.rstrip() + "!")
print()

curso = "Python"
print('Aumenta e centraliza a string usando o caracter especificado:', curso.center(20, "_")) # Se um caracter não for especificado, o Python usará espaços em branco.
print('Mistura o caracter escolhido na string:', "_".join(curso)) # Mais usado em listas / PATHs / diretórios etc.