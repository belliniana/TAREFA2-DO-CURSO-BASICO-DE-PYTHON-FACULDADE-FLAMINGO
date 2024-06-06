#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 3) Faça um programa que pergunte ao usuário o valor do produto e o percentual 
# de desconto, e retorne o valor final após o desconto.

valor_produto=float(input("Digite o valor do produto: "))
percentual_desconto=float(input("Digite o percentual de desconto: "))
valor_desconto =valor_produto*(percentual_desconto/100)
valor_final=valor_produto-valor_desconto
print("O valor final após o desconto é: R$", valor_final)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")