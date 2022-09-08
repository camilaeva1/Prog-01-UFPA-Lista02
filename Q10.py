# Questão 10: Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
n1 = float(input("Insira a primeira nota parcial: "))
n2 = float(input("Insira a segunda nota parcial: "))
n3 = float(input("Insira a terceira nota parcial: "))
media = (n1 + n2 + n3)/3
if media == 10:
  conc = "Aprovado com Distinção"
elif media >= 7 and media != 10:
  conc = "Aprovado"
elif media < 7:
  conc = "Reprovado"
print(conc)