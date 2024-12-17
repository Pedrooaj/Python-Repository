nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
if nome and idade:
    print(f"Seu nome e: {nome}")
    print(f"Seu nome invertido e: {nome[::-1]}")
    print(f"Seu nome contém espaços: {'sim' if ' ' in nome else 'não'}")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra de seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")
else:
    print("Desculpe, você deixou algum dos campos vazios!")

