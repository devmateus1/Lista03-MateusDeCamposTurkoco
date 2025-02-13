#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal
salario = float(input("Qual é seu salario:  "))

if salario <=  2259.20:
    print("Você esta isento.")
    
elif salario >= 2259.21 and salario <=  3751.05:
    imposto = salario * 0.075 
    print("Você irá pagar: ", imposto , "de imposto")  
    print("Mateus De Campos Turkoco")

elif salario >= 2826.66 and salario <= 3751.06:
    imposto = salario * 0.15
    print("Você irá pagar: ", imposto, "de imposto")
    print("Mateus De Campos Turkoco")

elif salario >=  3751.06 and salario <= 4664.68:
    imposto = salario * 0.225  
    print("Você irá pagar: ", imposto, "de imposto")
    print("Mateus De Campos Turkoco")

elif salario >= 4664.68:
    imposto = salario * 0.275 
    print("Você irá pagar: ", imposto, "de imposto") 
    print("Mateus De Campos Turkoco")