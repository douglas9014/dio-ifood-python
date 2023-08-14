nome = input("Qual é o seu nome? ") # Essa função é utilizada para receber dados de entrada inseridos pelo usuário.
sobrenome = input("E o seu sobrenome? ")
print(f"\nOi, {nome} {sobrenome}!\n\n")

print(nome, sobrenome) # print() termina com "\n" e tem por padrão separação por espaço em branco.
print(nome, sobrenome, end=".\n----------\n") # "end" é usado para se definir uma forma diferente para finalizar um print().
print(nome, sobrenome, sep="_") # "sep" define um separador para se usar no lugar do espaço em branco.
print()