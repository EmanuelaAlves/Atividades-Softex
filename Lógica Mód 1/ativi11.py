def calculadora(op1, op2, operacao):
    if operacao == 1:
        return op1 + op2
    if operacao == 2:
        return op1 - op2
    if operacao == 3:
        return op1 * op2
    if operacao == 4:
        return op1 / op2
        
execute = True
while execute:
    print("Opções válidas:")
    print("1: soma")
    print("2: subtracao")
    print("3: multiplicacao")
    print("4: divisao")
    print("0: sair")
    oper = int(input("Informe a operacao: "))
    if oper >= 1 and oper  <= 4:
        op1 = int(input("Informe o primeiro operacao: "))
        op2 = int(input("Informe o segundo operacao: "))
        
        resultado = print(op1, op2, oper)
        print(resultado)
    if oper == 0:
        print("obrigada")
        execute = False
    else:
        print("Essa opção não exite.")