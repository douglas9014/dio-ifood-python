menu = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

Por favor, selecione uma opção informando uma letra conforme o menu acima.
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_operacao = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        # Não permitir depósitos negativos.
        # Registrar operação no extrato.
        
        print("Selecionado: [ DEPÓSITO ]")
        while True:
            print("Digite ""0"" (zero) para voltar ao menu inicial.\n")
            valor_operacao = float(input("Informe o valor para ser depositado: "))

            if valor_operacao > 0:
                saldo += valor_operacao
                extrato += f"Depósito: R$ {valor_operacao:.2f}\n"
                print(f"Depositado: R$ {valor_operacao:.2f}")
                print(f"Saldo atual: R$ {saldo:.2f}\n")
                break

            elif valor_operacao == 0:
                print("Operação cancelada!")
                break

            else:
                print("Valor inválido! Por favor, verifique e tente novamente.\n")


    elif opcao == "s":
        # Limite de 3 operações de saque.
        # Limite de R$ 500,00 por operação de saque.
        # Se o saldo for insuficiente, informar ao usuário e não executar a operação de saque.
        # Registrar operação no extrato.

        print("Selecionado: [ SAQUE ]\n")
        while numero_saques < 3:
            print("Você possui", LIMITE_SAQUES - numero_saques, "operação(ões) de saque restante(s).")
            print(f"Cada operação de saque não pode exceder R$ {limite:.2f}.")
            print("\nDigite ""0"" (zero) para voltar ao menu inicial.\n")

            valor_operacao = float(input("Informe o valor para ser sacado: "))

            if valor_operacao > 0:
                if valor_operacao > limite:
                        print("Limite de saque excedido! Por favor, escolha um valor menor e tente novamente.\n")
                
                elif valor_operacao > saldo:
                    print("Saldo insuficiente! Por favor, confira o seu extrato e tente novamente.\n")

                else:
                    numero_saques += 1
                    saldo -= valor_operacao
                    extrato += f"Saque: R$ {valor_operacao:.2f}\n"
                    print(f"Sacado: R$ {valor_operacao:.2f}")
                    print(f"Saldo atual: R$ {saldo:.2f}\n")

            elif valor_operacao == 0:
                print("Operação cancelada!")
                break

            else:
                print("Valor inválido! Por favor, verifique e tente novamente.\n")
    
        print("Quantidade diária de operações de saque esgotada. Tente novamente mais tarde.\n")


    elif opcao == "e":
        # Listar todos os depósitos e saques realizados.
        # No fim da listagem deve-se exibir o saldo atual.
        # Os valores devem ser exibidos no seguinte formato: R$ xxxx.xx
        # Exemplo: R$ 1570.90
        print("Selecionado: [ EXTRATO ]\n")

        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato de operações da conta:")
            print(extrato)
        
        print(f"Saldo atual = R$ {saldo:.2f}")


    elif opcao == "q":
        print("Sessão encerrada. Até mais!\n")
        break


    else:
        print("Opção inválida! Por favor, tente novamente.")