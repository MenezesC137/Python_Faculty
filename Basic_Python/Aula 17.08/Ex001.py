num1 = int(input("Digite o primeiro valor da operação: "))
num2 = int(input("Digite o segundo valor da operação: "))

operacao = input("Qual operação voce deseja realizar? \n 1-Adição(+) \n 2-Subtração(-) \n 3-Multiplicação(*) \n 4-Divisão(/)\n :")

total = 0

if operacao == "1":
    total = num1 + num2
    print(f"A operação: {num1} + {num2} = {total}")
elif operacao == "2":
    total = num1 - num2
    print(f"A operação: {num1} - {num2} = {total}")
elif operacao == "3":
    total = num1 * num2
    print(f"A operação: {num1} * {num2} = {total}")
elif operacao == "4":
    total = num1 / num2
    print(f"A operação: {num1} / {num2} = {total}")
else:
    print("Operação inválida!")
    




