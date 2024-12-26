while True:
    try:
        n = int(input("Digite um número inteiro: \n"))
        if n%2 == 0:
            print("Este número e par!")
        else:
            print("Este número e impar!")
        break
    except:
        print("Valor inválido!")