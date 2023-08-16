heroisM = ["Homem Aranha", "Hulk", "Gavião Arqueiro", "Homem de Ferro", "Wanda"]
heroisD = ["Super Homem", "Mulher Maravilha", "Batman", "Flash", "Aquaman"]



universo = input("Digite um universo de heróis: ")
if universo == "Marvel":
    print("Você escolheu Marvel")
    herois = input("Digite um Herói da Marvel: ")
    if herois in heroisM:
        n = int(input("Quantas vezes quer que repita? "))
        contador = 0
        while(contador < n):
            contador = contador + 1
            print(herois)
    else:
        print("Herói não encontrado :(")
elif universo == "DC":
    print("Você escolheu DC")
    herois = input("Digite um Herói da DC: ")
    if herois in heroisD:
        n = int(input("Quantas vezes quer que repita? "))
        contador = 0
        while(contador < n):
            contador = contador + 1
            print(herois)
else:
    print("Universo não encontrado")