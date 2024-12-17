"""
Formatação básica
s - string
d - int
f - float 
.<digitos decimais apos a virgula>f
x ou X - hexadecimal
> - direita
< - esquerda
^ - centro
sinal - + ou -

"""


variavel = 'ABC'

print(f'{variavel: <10}')
print(f'{variavel:->10}')
print(f'{variavel:-^10}')