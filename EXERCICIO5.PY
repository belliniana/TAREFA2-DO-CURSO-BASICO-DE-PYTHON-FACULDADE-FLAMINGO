#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 5)Crie um programa que pergunte ao usuário a quantidade de
# dias, horas, minutos e segundos, e calcule o total em segundos.

dia=int(input("Digite a quantidade de dias: "))
hora=int(input("Digite a quantidade de horas: "))
minuto=int(input("Digite a quantidade de minutos: "))
segundo=int(input("Digite a quantidade de segundos: "))
total_segundo = (dia*24*3600)+(hora*3600)+(minuto*60)+segundo
print("O total em segundos é:", total_segundo)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")