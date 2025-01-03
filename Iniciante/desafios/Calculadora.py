"""Calculadora while"""

while True: 
    print("Calculadora de Pedrooaj v0.1")
    n1 = input('Digite um número: \n')
    n2 = input('Digite outro número: \n')
    op = input('Digite a operador(+ - / *): \n')

    number_valid = None
    op_valid = "+-/*"
    n1_float = 0
    n2_float = 0


    # Faz a valição se os númeors digitados são validos
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        number_valid = True
    except:
        number_valid = None

    # Trata a exceção caso seja invalido
    if number_valid is None:
        print("Números digitados são inválidos.")
        continue

    # verifica se o operador e válido
    if op not in op_valid:
        print("Operador inválido")
        continue

    # verifica se foi digitado apenas um operador
    if len(op) > 1:
        print("Digite apenas um operador")
        continue
    
    result = None
    if op == "+":
        result = n1_float + n2_float
    elif op == "-":
        result = n1_float - n2_float
    elif op == "*":
        result = n1_float * n2_float
    elif op == "/":
        result = n1_float / n2_float
        
    if result is not None:
        print(f"Seu resultado e: {result}")    
        
    sair = input("Quer sair? [s]air \n").lower().startswith('s')
    
    if sair:
        break
    else:
        continue