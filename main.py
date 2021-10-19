""" Desafio 1 e Desafio 3"""

from Pessoa import *


def dados():
    nome = input("Informe seu Nome: ")
    idade = input("Informe sua idade (apenas números): ")
    sexo = input("Informe seu sexo: ")
    cidade = input("Informe a sua cidade: ")
    estado = input("Informe o seu estado: ")
    return nome, idade, sexo, cidade, estado
print(dados())


pessoa = Pessoa(input("Informe seu Nome: "),
                input("Informe sua idade (apenas números): "),
                input("Informe seu sexo: "),
                input("Informe a sua cidade: "),
                input("Informe o seu estado: "))

print("Olá " + pessoa.Nome + "!")
print(
    "Você tem " + pessoa.Idade + " anos, pertence ao sexo " + pessoa.Sexo + ", reside em " + pessoa.Cidade + ", estado de(o) "
    + pessoa.Estado + ".")
