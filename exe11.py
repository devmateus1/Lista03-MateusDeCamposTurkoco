#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
distancia = int(input("Que distancia você deseja percorrer em km ? "))
cobranca = distancia * 0.50
print("Você pagara : ", cobranca, "pela passagem")
print("Mateus De Campos Turkoco")

if distancia >= 200:
    cobranca = distancia * 0.45
    print("Você pagara : ", cobranca, "pela passagem")
    print("Mateus De Campos Turkoco")