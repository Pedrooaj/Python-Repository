"""
Constante = Variaveis imutaveis são uma convenção utilzamos letras maiusculas nela

Muitas condições e cadeias de if e else e ruim!

"""


velocidade = 61
local_carro = 99

# Constantes / Imutaveis
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1


if velocidade > RADAR_1 :
    print("Velocidade carro passou do radar 1")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print("Carro multado no radar 1")