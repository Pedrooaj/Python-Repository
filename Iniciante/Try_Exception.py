"""
Tratamento de exceções
try e exception equivale a try e catch 
"""
numero = input("Digite um número que sera 2x: ")

try:
    numero_float = float(numero)
    print(f'Resposta: O dobro de {numero} é {numero_float * 2:.2f}')
except:
    print('Isso não e um número')
