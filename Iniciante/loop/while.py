"""
Loop while (Enquanto a condição for True ele e executado)
"""

# while True:
#     nome = input("Qual seu nome? \n")
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':
#         break
# print("Você saiu")

# continue volta para o começo do laço sem parar ele

i = 0
while True:
    i += 1

    if i == 6:
        print("Não quero exibir o 6 pulei!")
        continue
    print(i)
    if i == 10:
        break

