# O operador "in" é utilizado para verificar se um objeto está presente em uma sequência.
# Cuidado! A comparação é case-sensitive (diferencia maiúsculas e minúsculas).

nome_curso = "Ciência de Dados com Python"
frutas = ['laranja', 'uva', 'morango', 'limão', 'abacaxi']
saques = [50, 100, 297, 44]

print("Python" in nome_curso)
print("curso" in nome_curso) # Atenção ao "c" minúsculo!
print('uva' in frutas)
print('maçã' in frutas)
print('tomate' not in frutas)
print(100 not in saques)