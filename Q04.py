#Questão 04: 4. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela
n1 = float(input("Insira a primeira nota parcial: "))
n2 = float(input("Insira a segunda nota parcial: "))
media = (n1 + n2)/2
if media <= 10 and media >= 9:
  entre = "9.0 e 10.0"
  conc = "A"
elif media < 9 and media >= 7.5:
  entre = "7.5 e 9.0"
  conc = "B"
elif media <= 7.5 and media >= 6:
  entre = "7.5 e 6.0"
  conc = "C"
elif media <= 6 and media >= 4:
  entre = "6.0 e 4.0"
  conc = "D"
elif media <= 4 and media >= 0:
  entre = "4.0 e 0.0"
  conc = "E"
else:
  print("Valor inválido")
print("MÉDIA DE APROVEITAMENTO                       CONCEITO")
print("Entre {}                                     {}".format(entre, conc))