conta_normal = True
conta_universitaria = False

saldo = 1500
saque = 2000
cheque_especial = 500

if conta_normal:
    if saldo >= saque:
        print('Saque realizado!')
    elif saque <= (saldo + cheque_especial):
        print("Saque com cheque especial realizado!")
    else:
        print("Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado!')
    else:
        print('Saldo insuficiente!')