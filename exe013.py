salario = float(input('Qual o valor do seu Salario atual? R$ '))
novo = salario + (salario * 15 / 100)
print('Um funcioario que ganhava R$ {:.2f} com o aumento de 15% passa a ganhar R$ {:.2f}'.format(salario, novo))