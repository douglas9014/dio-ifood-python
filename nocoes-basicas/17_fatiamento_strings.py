nome = 'Douglas Fernandes Oliveira'

# variável_string[inicio:fim:passos]

# Extrair somente um caracter:
print(nome[0])
print(nome[-1])
print(nome[-3])
print(nome[8], '\n')

print(nome[:7]) # Extrair somente os primeiros N caracteres.
print(nome[8:]) # Extrair a partir da posição especificada.
print(nome[8:18]) # Extrair somente o intervalo de caracteres especificado.
print(nome[8:18:3], '\n') # Somente a faixa de caracteres especificada, pulando a quantidade de caracteres especificada.

print(nome[::-1], '\n') # Inverter/espelhar a string.