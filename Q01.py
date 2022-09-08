#Questão 01: As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo): aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela: o salário antes do reajuste;  o percentual de aumento aplicado; 
# o valor do aumento; o novo salário, após o aumento.
sal = float(input("Insira o valor do salario do colaborador em R$: "))
if sal <= 280:
    i = 20
    i1 = sal*0.2
    sal1 = sal + i1
if sal > 280 and sal <= 700:
    i = 15
    i1 = sal*0.15
    sal1 = sal + sal*0.15
if sal > 700 and sal <= 1500:
    i = 10
    i1 = sal*0.1
    sal1 = sal + sal*0.1
else:
    i = 5
    i1 = sal*0.05
    sal1 = sal + sal*0.05
print("O salário do colaborador antes do reajuste era de R$ {}, o percentual de aumento foi de {}%, o aumento no salário foi de {}, e o valor do salário atualizado ficou de R${}".format(sal, i, i1, sal1))