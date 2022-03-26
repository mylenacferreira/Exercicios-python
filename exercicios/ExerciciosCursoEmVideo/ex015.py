# Alguel de Carros

km = float(input('Quantos km foram percorridos com o carro? '))
dias = int(input('Quantos dias foram alugados? '))
pagar = (60 * dias) + (0.15 * km)
print(f'Deverá ser pago por {dias} dias e {km}km rodados um total de R${pagar}')
