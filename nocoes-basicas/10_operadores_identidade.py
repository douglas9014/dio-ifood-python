# O operador "is" é utilizado para verificar se diferentes variáveis ocupam a mesma região de memória.

saldo = 1000
limite = 200
saque = limite

print(saldo is limite)
print(saldo is not limite)
print(saque is limite)
print(saque is not limite)