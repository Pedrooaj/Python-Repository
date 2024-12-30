"""
https://docs.python.org/3/library/stdtypes.html
Imutáveis que vimos: str,int,float,bool
"""

string = 'Pedro Antônio'

outra_variavel = f'{string[:2]}ABC{string[5:]}'

print(outra_variavel)

print(string.zfill(100))