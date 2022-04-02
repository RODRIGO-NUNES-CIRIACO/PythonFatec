import string


# aspas duplas
"todos os sapos pulam os rio"

# aspas simples
'nem todos os rios são quentes'

# aspas triplas duplas: permite quebra de linha
""""mas todos os quentes são rios"""

# as triplas simple: permite quebra de linha
''''e todos os sapos são amfíbios.'''

# string por função
# input("Digite seu nome: ")


# pedindo dados para o usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# print("Olá, ", nome, "você tem", idade, "anos")
print(f"Olá, {nome.title()}. você tem {idade} anos ")

