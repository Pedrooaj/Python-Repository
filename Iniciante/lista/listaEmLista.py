"""Lista em listas são comumente conhecidas como matriz"""

salas = [
    ["Pedro", "João", "Maria"],
    ["Alisson", "Carlos", "Odivan"],
    ["Gabriel", "Kessio", "Robbyson"]
]


print(salas[1][0] + "\n")

print("Lista de alunos!!")

for sala in salas:
    for aluno in sala:
        print(aluno)