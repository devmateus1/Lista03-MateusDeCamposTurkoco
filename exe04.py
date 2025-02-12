#Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho",
#"VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho", caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
cor = (input("Digite sua cor favorita: "))
cor1 = cor.title()
if cor == 'Vermelho':
    print("Eu também gosto de vermelho")
    print("Mateus De Campos Turkoco")
else:
    print("Eu não gosto desta", cor1 ,"cor:")
    print("Mateus De Campos Turkoco")

    