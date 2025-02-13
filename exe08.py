#Escreva um programa que pergunte a velocidade do carro de um usuário.
#  Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = int(input("Qual a velocidade do seu carro ?  "))
 
if velocidade > 80:
    ultra = velocidade - 80
    multa = ultra * 5
    print("Você foi multado em :", multa , "reais")
    print("Mateus De Campos Turkoco")
    
    