#Par ou Ímpar: Escreva um programa que receba um número inteiro e imprima se ele é par ou ímpar.

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
  print(f"O número {num} é par!")
else:
  print(f"O número {num} é ímpar!")