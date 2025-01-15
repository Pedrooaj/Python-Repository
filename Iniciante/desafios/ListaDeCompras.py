lista = []

while True: 
    resposta = input("Lista de Compras\n[i]nserir [a]pagar [l]istar: ").lower()
    
    if resposta == 'i':
        lista.append(input("Digite o item que deseja adicionar: "))
    elif resposta == 'a':
        ...
    elif resposta == 'l':
        print("Listando o carrinho de compras")
        for i in range(len(lista)):
            print(f"{i} {lista[i]}")
    