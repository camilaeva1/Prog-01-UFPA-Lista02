# Questão 18. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. 
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 
carne = str(input("Qual tipo de carne vc comprará (File Duplo - FD, Alcatra - AL, Picanha - PI)?  "))
kg = int(input("Quantos kg de carne vc levará?  "))
cartao = str(input("Vc vai pagar com o cartão Tabajara (S/N)?  "))
if carne == 'FD':
  c = "Filé Duplo"
  if kg <= 5:
    preco = 4.9 * kg
  else:
    preco = 5.8 * kg
if carne == 'AL':
  c = "Alcatra"
  if kg <= 5:
    preco = 5.9 * kg
  else:
    preco = 6.8 * kg
if carne == 'PI':
  c = "Picanha"
  if kg <= 5:
    preco = 6.9 * kg
  else:
    preco = 7.8 * kg
print(preco)
if cartao == 'S':
  pag = "CARTÃO"
  desc = preco * 0.05
  preco = preco - desc
else:
  pag = "DINHEIRO"
  preco = preco
print("*********CUPOM FISCAL**********")
print("TIPO DE CARNE: {}".format(c))
print("FORMA DE PAGAMENTO:  {}".format(pag))
print("VALOR DO DESCONTO:  {:.2F}".format(desc))
print("VALOR TOTAL  R$ {:.2f}.".format(preco))