operacao = input("Digite a operacao desejada (soma, sub, mult,div): ")
num1 = input("Digite primeiro número: ")
num2 = input("Digite o segundo número: ")

if operacao == "soma":
        resultado =  int(num1) + int(num2)
if operacao == "sub":
        resultado =  int(num1) - int(num2)
if operacao == "mult":
        resultado =  int(num1) * int(num2)
if operacao == "div":
        resultado =  int(num1) / int(num2)
else: 
        resutado = "Operação inválida."
print("O resultado da operação é: " + str(resultado))