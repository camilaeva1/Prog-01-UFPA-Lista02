# Questão 17: Uma fruteira está vendendo frutas com a seguinte tabela de preços descrita no problema;
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
morango = float(input("Quantos kg de morango vc quer levar? "))
if morango <= 5:
  preco1 = morango * 2.5
else:
  preco1 = morango * 2.2
maca =float(input("Quantos kg de maçã vc quer levar? "))
if maca <= 5:
  preco2 = maca * 1.8
else:
  preco2 = maca * 1.5
totalkg = morango + maca
total = preco1 + preco2
if totalkg >= 8 or total >= 25:
  total = total - (total * 0.10)
print("O valor que o cliente pagará já com desconto final é de R$ {:.2f}.".format(total))