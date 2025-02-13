#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
salario = float(input("Qual o seu salario ? "))
if salario >= 1.251:
    aumento = salario * 0.10
    print("Seu aumento será de : ", aumento, "reais")
    print("Mateus De Campos Turkoco")

elif salario <= 1.250:
    aumento = salario * 0.15
    print("Seu aumento será de : ", aumento, "reais")
    print("Mateus De Campos Turkoco")

