nome = str(input("Digite seu nome: "));
altura = float(input("Digite sua altura: "));
peso = float(input("Digite seu peso: "));
# elipissis ... print(...) 
imc = peso / altura ** 2;
print(f'Nome: {nome} \nAltura: {altura}\nPeso: {peso} \nImc: {round(imc, 2)}');