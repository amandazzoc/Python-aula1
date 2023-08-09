heroisM = ["Homem Aranha", "Hulk", "Gavião Arqueiro", "Homem de Ferro", "Wanda"]
heroisD = ["Super Homem", "Mulher Maravilha", "Batman", "Flash", "Aquaman"]

universos = ["Marvel", "DC"]

universo = input("Digite um universo de heróis: ")
if universo == universos[0]:
    print("Você escolheu Marvel")
    herois = input("Digite um Herói da Marvel: ")
elif universo == universos[1]:
    print("Você escolheu DC")
    herois = input("Digite um Herói da DC: ")
else:
    print("Universo não encontrado")