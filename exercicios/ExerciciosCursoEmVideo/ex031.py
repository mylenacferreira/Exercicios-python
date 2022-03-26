# Calcule um programa que receba a distancia de uma viagem, calcule o preço da passagem cobrando 0.5
# por km para viagens ate 200km e e 0.45 para mais longas

dist = float(input('Digite por favor a distância da sua viagem, em Km: '))

if dist <= 200:
    valor = dist * 0.5
else:
    valor = dist * 0.45
print('O valor da sua passagem é de R${:.2f}'.format(valor))
