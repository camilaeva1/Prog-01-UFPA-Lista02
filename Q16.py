# Questão 16. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:até 20 litros, desconto de 3% por litro,  acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro,  acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
comb = str(input("Com qual o combustível vc deseja abastecer (A/G)? "))
litros = int(input("Quantos litros vc vai abastecer? "))
if comb == 'A':
  if litros >= 20:
    desc = 0.05
  else:
    desc = 0.03
pagar = (litros * 1.9)
total = pagar - (pagar*desc)
print("Total a pagar com desconto é R$ {:.2f}.".format(total))
if comb == 'G':
  if litros >= 20:
    desc = 0.06
  else:
    desc = 0.04
pagar = (litros * 2.5)
total = pagar - (pagar*desc)  
print("Total a pagar com desconto é R$ {:.2f}.".format(total)) 
    