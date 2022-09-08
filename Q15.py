# Questão 15. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: m. "Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
r1 = str(input("Telefonou para a vítima?(S/N) "))
r2 = str(input("Esteve no local do crime?(S/N) "))
r3 = str(input("Mora perto da vítima?(S/N) "))
r4 = str(input("Devia para a vítima?(S/N) "))
r5 = str(input("Já trabalhou com a vítima?(S/N) "))
cont = 0
if r1 == 'S':
  cont = cont + 1
if r2 == 'S':
  cont = cont + 1
if r3 == 'S':
  cont = cont + 1
if r4 == 'S':
  cont = cont + 1
if r5 == 'S':
  cont = cont + 1
if cont >= 5:
  print("ASSASSINO")
if cont >=3 and cont <= 4:
  print("CÚMPLICE")
if cont == 2:
  print("SUSPEITA")