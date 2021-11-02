larg = float(input('Qual a largura da sua parede ?'))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
print('Sua parede tem dimensoes de {}x{} e sua área é de {}'.format(larg, alt, area))
tinta= area / 2
print('Para pintar essa parede você precisara de {}L de tinta'.format(tinta))