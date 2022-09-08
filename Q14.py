# Questão 14: Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
op = str(input("Qual operação vc deseja reslizar (+, -, /, x): "))
if op == '+':
  n3 = n1 + n2
elif op == '-':
  n3 = n1 - n2
elif op == '/':
  n3 = n1/n2
elif op == 'x':
  n3 = n1*n2
else:
  print("Símbolo inválido")
if n3 % 2 == 0:
  print("O resultado é par")
else:
  print("O resultado é ímpar")
if n3 > 0:
  print("O resultado é positivo")
else:
  print("O resultado é negativo")
if n3 == round(n3):
  print("O resultado é um número inteiro")
else:
  print("O resultado é um número decimal")

