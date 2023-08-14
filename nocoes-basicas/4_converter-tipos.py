print("Convertendo os tipos de variáveis:")
preco = 11
print("Inteiro:", int(preco))
print("Float:", float(preco))
print("Float usando divisão:", preco / 2)
print("Inteiro usando divisão:", preco // 2)
print("String:", str(preco), "\n")

texto = "Este texto não é um número!"
print("Tipo da variável:", type(texto), "\n") # A função "type()" é usada para identificar o tipo de uma variável.

print("Nem sempre é possível converter os tipos das variáveis. Veja essa mensagem de erro:")
print(float(texto))