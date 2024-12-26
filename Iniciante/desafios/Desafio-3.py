

while True:
    nome = input("Digite seu nome: \n")
    if nome:
        if len(nome) <= 4:
            print("Seu nome e muito curto")
            break
        elif len(nome) > 4 and len(nome) <= 6:
            print("Seu nome e normal")
            break
        else:
            print("Seu nome e muito grande")
            break
    else:
        print("Por favor, digite seu nome")