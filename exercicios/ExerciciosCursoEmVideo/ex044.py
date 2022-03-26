normal = float(input('Digite o preço atual do produto: R$'))
cond = int(input('Digite qual a forma de pagamento, sendo\n1 - À vista no dinheiro\n2 - À vista no cartão\n3 - 2x no '
                 'cartão\n4 - 3x ou mais no cartão: '))

if cond == 1:
    desc = normal * 0.9
    print(f'Com pagamento à vista no dinheiro você pagou 10%, pagará apenas R${desc}')
elif cond == 2:
    desc = normal * 0.95
    print(f'Com pagamento à vista no cartão você pagou 5%, pagará apenas R${desc}')
elif cond == 3:
    parcela = normal / 2
    print(f'Com pagamento em 2x no cartão, você pagará R${parcela:.2f} em cada parcela totalizando R${normal}')
elif cond == 4:
    vezes = int(input('Em quantas parcelas você deseja pagar?: '))
    desc = normal * 1.2
    parcela = desc / vezes
    print(f'Com pagamento em 3x ou mais no cartão você pagará R${parcela:.2f} em cada parcela totalizando'
          f'R${desc:.2f}')
else:
    print('Erro na compra')
