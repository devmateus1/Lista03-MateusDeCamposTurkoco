#Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite.
#  Se ele responder "sim", pergunte se está ventando. Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva",
#  caso contrário, exiba a mensagem "Pegue um guarda-chuva". Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".
chuva = (input("Esta chovendo ? ").lower)

if chuva == "SIM".lower():
    vento = input("Esta ventando ? ").lower()
    if vento == "SIM":
        print("Está ventando muito para um guarda-chuva")
        print("Mateus De Campos Turkoco")

    elif vento == "NÂO":
        print("Pegue um guarda-chuva")
        print("Mateus De Campos Turkoco")

    else:
        print("Aproveite o seu dia")     
        print("Mateus De Campos Turkoco")  
    
        

    
