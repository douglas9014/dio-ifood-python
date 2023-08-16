nome = 'Douglas'
idade = 31
profissao = 'Desenvolvedor'
linguagem = 'Python'
dados = {"nome": "Douglas", "idade": 31, "profissao": "Desenvolvedor", "linguagem": "Python"}
print()

# Forma antiga: %
print("Oi, meu nome é %s. Eu tenho %d de idade, trabalho como %s e estou matrículado no curso de %s." % (nome, idade, profissao, linguagem))

# Forma antiga: format
print("Oi, meu nome é {}. Eu tenho {} de idade, trabalho como {} e estou matrículado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Oi, meu nome é {3}. Eu tenho {0} de idade, trabalho como {2} e estou matrículado no curso de {1}.".format(idade, linguagem, profissao, nome)) # Útil quando precisa-se utilizar uma mesma variável várias vezes na mesma string.
print("Oi, meu nome é {nome_usuario}. Eu tenho {idade_anos} de idade, trabalho como {profissao_atual} e estou matrículado no curso de {linguagem_curso}.".format(nome_usuario=nome, idade_anos=idade, profissao_atual=profissao, linguagem_curso=linguagem))
print("Oi, meu nome é {nome}. Eu tenho {idade} de idade, trabalho como {profissao} e estou matrículado no curso de {linguagem}.".format(**dados))

# Forma recomendada: f-string
print(f"Oi, meu nome é {nome}. Eu tenho {idade} de idade, trabalho como {profissao} e estou matrículado no curso de {linguagem}.") # Atenção ao "f" no lá antes da string!
print()

# Formatar strings com f-string:
PI = 3.1415926535
print(f'Pi = {PI}')
print(f'Pi = {PI:10.2f}') # Os números especificam casas à esquerda e à direita.