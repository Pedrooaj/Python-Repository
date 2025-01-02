name = input("Digite seu nome: \n")

contador = 0

new_name = ""

while contador < len(name):
    if contador + 1 == len(name):
        new_name += name[contador] 
    else:
        new_name += name[contador] + "*"
    contador += 1

print(new_name)