# O Python exige que o código seja identado para identificar os blocos de código. Caso contrário, o código não funcionará.
saldo = 500
print()

def sacar(valor, saldo):
    if saldo >= valor:
        print('Valor sacado:', valor)
        saldo -= valor
        print('Novo saldo:', saldo)
        print('Retire o dinheiro.')

def depositar(valor, saldo):
    print('Valor depositado:', valor)
    saldo += valor
    print('Novo saldo:', saldo)

# sacar(100, saldo)
depositar(100, saldo)
print("Obrigado! Até mais.\n")