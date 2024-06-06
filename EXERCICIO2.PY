#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 2) Crie um programa que solicite ao usuário sua 
# altura e peso, e calcule seu índice de massa corporal (IMC).

altura=float(input("Digite sua altura em metros (ex: 1.75): "))
peso=float(input("Digite seu peso em quilogramas (ex: 70.5): "))
imc=peso/(altura**2)
print("Seu IMC é:", imc)
if imc<18.5:
    print("Você está abaixo do peso ideal.")
elif 18.5<=imc<24.9:
    print("Você está no peso ideal.")
elif 25<=imc<29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
print("\nClassificação do IMC:")
print("Abaixo de 18.5: Abaixo do peso")
print("Entre 18.5 e 24.9: Peso normal")
print("Entre 25 e 29.9: Sobrepeso")
print("30 ou acima: Obesidade")
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")