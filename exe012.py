preço= float(input('Qual o valor do Produto que você deseja? R$ '))
novo = preço - (preço * 7 / 100)
print('O produto que custava {:.2f} , na Promoção com 5% vai custar {:.2f} '.format(preço,novo))