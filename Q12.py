# Questão 12: Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).
valor = int(input("Insira um número: "))
if valor % 2 == 0:
  print("O número é par.")
else:
  print("O número é ímpar.")