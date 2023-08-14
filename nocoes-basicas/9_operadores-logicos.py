saldo = 1500
saque = 200
limite = 100
conta_especial = True

print(saldo >= saque and saque <= limite) # Operador "E" (and): retorna verdadeiro somente se ambas expressões retornam verdadeiro.
print(saldo >= saque or saque <= limite) # Operador "OU" (or): retorna verdadeiro quando qualquer das expressões retornam verdadeiro.

print('\n--------------------\n')

# Parênteses nem sempre são necessários, mas melhoram muito a leitura do código:
saque_aprovado = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # "Se for conta especial, ignore o limite."
print('Saque aprovado?', saque_aprovado)

# O uso de variáveis para identificar partes do código facilitam o entendimento dele:
saque_aprovado_conta_comum = (saldo >= saque and saque <= limite)
saque_aprovado_conta_especial = (conta_especial and saldo >= saque)
saque_aprovado_resultado = (saque_aprovado_conta_comum or saque_aprovado_conta_especial)
print('Saque aprovado?', saque_aprovado_resultado)

print('\n--------------------\n')

# Operador de negação (not): inverte o resultado da comparação.
lista_vazia, texto = [], "Algum texto!" # Sequencias/variáveis vazias retornam falso.

print('NOT:')
print('Comparação:', not 1500 > 2000)
print('Lista vazia (false):', not lista_vazia)
print('Texto vazio (true)', not texto)