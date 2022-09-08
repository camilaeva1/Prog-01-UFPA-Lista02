# Questão 13: Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
valor = float(input("Insira um número: "))
if valor == round(valor):
  print("O número é inteiro.")
else:
  print("O número é decimal.")