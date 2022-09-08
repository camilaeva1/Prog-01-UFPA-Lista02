# Questão 11: Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
valor = int(input("Qual valor do saque R$: "))
if valor > 10 and valor < 600:
  cem = valor // 100
  resto1 = valor % 100
  print("Notas de cem ", cem)
  if resto1 != 0:
    cinq = resto1 // 50
    resto2 = resto1 % 50
    if cinq != 0:
      print("Notas de cinquenta ", cinq)
    if resto2 != 0:
      dez = resto2 // 10
      resto3 = resto2 % 10
      if dez != 0:
        print("Notas de dez ", dez)
      if resto3 != 0:
        cinco = resto3 // 5
        resto4 = resto3 %5
        if cinco != 0:
            print("Notas de cinco ", cinco)
            if resto4 != 0:
              print("Notas de um ", resto4)
else:
    print("Digite um valor válido")