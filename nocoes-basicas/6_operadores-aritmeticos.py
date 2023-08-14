produto_1 = 10
produto_2 = 7
produto_3 = 2

print("Adição:", produto_1 + produto_2)
print('Subtração:', produto_1 - produto_2)
print('Multiplicação:', produto_1 * produto_2)
print('Divisão com flutuante:', produto_1 / produto_2) # Resultado em float
print('Divisão com inteiro:', produto_1 // produto_2) # Resultado em int
print('Módulo:', produto_1 % produto_2) # Resto da divisão
print('Exponenciação:', produto_1 ** produto_2)

# Os cálculos em expressões matemáticas seguem a seguinte ordem:
# 1º Parêntesis
# 2º Expoêntes
# 3º Multiplicações e Divisões
# 4º Adições e Subtrações

# Exemplos:
print('\nParêntesis:', (produto_1 - produto_2) * produto_3)
print('Direto:', produto_1 - produto_2 * produto_3)