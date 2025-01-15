"""
enumerate - enumera iteraveis(índices)
"""

lista = ["Maria", "Helena", "Luiz"]

lista.append("João")

print(list(enumerate(lista)))

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
    
print("\n")
    
for indice, valor in enumerate(lista):
    print(indice, nome)