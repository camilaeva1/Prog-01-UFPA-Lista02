#Questão 02: 2. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR: Salário Bruto até 900 (inclusive) - isento, Salário Bruto até 1500 (inclusive) - desconto de 5%, Salário Bruto até 2500 (inclusive) - desconto de 10%, ◦ Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
h = int(input("Insira horas foram trabalhadas no mês de referência R$: "))
vh = float(input("Insira o valor pago por hora ao colaborador R$: "))
sb = h * vh
print(sb)
if sb <= 900:
  i = 0
  sbir = 0
  sb = sb
if sb > 900 and sb <= 1500:
  i = 5
  sbir = sb*0.05
if sb > 1500 and sb <= 2500:
  i = 10
  sbir = sb*0.1
if sb > 2500:
  i = 20
  sbir = sb*0.2
inss = sb * 0.10
fgts = sb * 0.11
td = sbir + inss
sl = sb - td
print("SALÁRIO BRUTO ({} * {})                              : R$ {}".format(vh, h, sb))
print("   (-) IR ({}%)                                      : R$ {}".format(i, sbir))
print("   (-) INSS (10%)                                    : R$ {}".format(inss))
print("   FGTS (11%)                                        : R$ {}".format(fgts))
print("   Total de descontos                                : R$ {}".format(td))
print("   Salário Líquido                                   : R$ {}".format(sl))