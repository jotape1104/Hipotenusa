from math import hypot
cat_o = float(input('Valor do cateto oposto: '))
cat_a = float(input('Valor do cateto adjacente: '))
hip = hypot(cat_o, cat_a)
print('O valor da hipotenusa é {:.2f}'.format(hip))
