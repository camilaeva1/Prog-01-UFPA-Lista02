#Questão 03: Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
dia = int(input("Insira o número correspondente ao dia da semana (1 - Domigo, 2 - Segunda...): "))
if dia == 1:
  print("DOMINGO")
elif dia == 2:
  print("SEGUNDA")
elif dia == 3:
  print("TERÇA-FEIRA")
elif dia == 4:
  print("QUARTA-FEIRA")
elif dia == 5:
  print("QUINTA-FEIRA")
elif dia == 6:
  print("SEXTA-FEIRA")
else:
  print("Valor inválido")
