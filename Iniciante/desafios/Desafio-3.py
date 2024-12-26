nome = input("Digite seu nome: \n")

if len(nome) <= 4:
    print("Seu nome e muito curto")
elif len(nome) > 4 and len(nome) <= 6:
    print("Seu nome e normal")
else:
    print("Seu nome e muito grande")