# Questão 9: Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
n1 = int(input("Insira um número: "))
n2 = str(n1)
print("O número possui {} centenas, {} dezenas e {} unidades".format(n2[0], n2[1], n2[2]))