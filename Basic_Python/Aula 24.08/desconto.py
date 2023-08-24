valor_compra = float(input("Digite o valor da compra: "))
desconto = 0

if valor_compra > 100:
    desconto = valor_compra * 0.1
    valor_compra = valor_compra - desconto
    print(f"O valor da compra com desconto é: R$ {valor_compra}")
else:
    print(f"O valor da compra é: R$ {valor_compra}")
