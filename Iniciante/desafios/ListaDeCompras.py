lista = []

while True: 
    resposta = input("Lista de Compras\n[i]nserir [a]pagar [l]istar: ").lower()
    print("-" * 40)
    if resposta == 'i':
        lista.append(input("Digite o item que deseja adicionar: "))
        print("-" * 40)
    elif resposta == 'a':

        try:
            indice = int(input("Escolha um indice para apagar: "))
            del lista[indice]
            print("Item deletado com sucesso")  
            print("-" * 40)
        except ValueError:
          print('O indice deve ser um número inteiro')
          print("-" * 40)
        except IndexError:
            print("Indice não existe")
            print("-" * 40)
        except Exception:
            print("Erro desconhecido")
    elif resposta == 'l':
        if len(lista) > 0:
            print("Listando o carrinho de compras")
            print("-" * 40)
            for i in range(len(lista)):
                print(f"{i} {lista[i]}")
        else:
            print("Nada pra listar")
        print("-" * 40)
    