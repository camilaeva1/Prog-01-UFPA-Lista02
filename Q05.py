#Questão 05: Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
l1 = float(input("Insira o primeira lado: "))
l2 = float(input("Insira o segundo lado: "))
l3 = float(input("Insira o terceiro lado: "))
if (l1 + l2) > l3 or (l2 + l3) > l1:
  print("Os três lados formam um triângulo: ")
  if l1 != l2 != l3:
    tri = "Escaleno"
  elif l1 == l2 == l3:
    tri = "Equilátero"
  else:
    tri = "Isosceles" 
print(tri)