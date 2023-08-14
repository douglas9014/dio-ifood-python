while True: # Loop infinito
    numero = input("Qual é o número??? ")
    
    if numero.isnumeric() and (int(numero) == 9):
        break
    elif numero.isalpha():
        print('Não sabe brincar...')

print('Acertou!')