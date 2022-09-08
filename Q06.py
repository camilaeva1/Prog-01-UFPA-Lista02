import math
#Questão 06. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações: 
# a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# d. Se o delta for positivo, a equação possui duas raizes reais; informe-as ao usuário;
a = float(input("Insira o valor de a: "))
if a != 0:
  b = float(input("Insira o valor de b: "))
  c = float(input("Insira o valor de c: "))
  d = (b*b) - (4*a*c)
  
  if d < 0:
    print("Esta equação não possui raízes reais.")
  elif d == 0:
    r1 = -b/(2*a)
    print("A raíz da equação vale {:.2f}.".format(r1))
  else:
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    print("As raízes da equação valem {:.2f} e {:.2f}.".format(r1, r2))
else:
  print("Esta equação não é do 2º grau.")