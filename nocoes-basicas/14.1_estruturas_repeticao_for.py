# Exemplo "for": Extrair vogais do texto.
texto = input('Digite alguma palavra: ')
VOGAIS = "AEIOU"

print('Vogais: ', end="")
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print('\n') # Executa no final da repetição do 'for'.