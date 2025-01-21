"""
split e join com list e str
split - divide uma string
join - une uma string

strip - corta espaço da linha
"""

frase = 'Olha só que, coisa interessante'
lista_frases = frase.split(",")


lista_frases_fixed = []

for i, frase in enumerate(lista_frases):
    lista_frases_fixed.append(lista_frases[i].strip())

print(lista_frases)
print(lista_frases_fixed)