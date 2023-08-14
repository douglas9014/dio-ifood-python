opcao = -1

while opcao != 0:
    opcao = int(input("[1] Saque \n[2] Depósito \n[3] Extrato \n[0] Sair \n"))

    if opcao == 1:
        print('\nSaque realizado.\n')
    elif opcao == 2:
        print('\nDepósito registrado.\n')
    elif opcao == 3:
        print('\nExtrado emitido.\n')
    elif opcao == 0:
        print('\nSessão encerrada.\n')
    else:
        print('\nOpção inválida...\n')