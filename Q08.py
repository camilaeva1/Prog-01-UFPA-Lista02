# Questão 8: Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia = int(input("Insira o dia (dd): "))
mes = int(input("Insira o mês (mm): "))
ano = int(input("Insira o ano (aaa): "))

if ano > 0 and ano <= 9999:
  if mes > 0 and mes <=12:
    if dia >= 1 and dia <= 31:
      print("Data válida")
    else:
      print("Data inválida")
  else:
    print("Data inválida")
else:
  print("Data inválida")