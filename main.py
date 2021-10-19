""" Desafio 1 e Desafio 3"""


def dados():
    nome = input("Informe seu Nome: ")
    idade = input("Informe sua idade (apenas números): ")
    sexo = input("Informe seu sexo: ")
    cidade = input("Informe a sua cidade: ")
    estado = input("Informe o seu estado: ")
    return nome, idade, sexo, cidade, estado


pessoa = dados()

print("Olá " + pessoa[0] + "!")
print(
      "Você tem " + pessoa[1] + " anos, pertence ao sexo " + pessoa[2] + ", reside em " + pessoa[3] + ", estado de(o) "
      + pessoa[4] + ".")
