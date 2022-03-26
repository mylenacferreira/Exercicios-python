altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Seu IMC é de {imc} você esta ABAIXO DO PESO')
elif 18.5 < imc <= 25:
    print(f'Seu IMC é de {imc} você esta com o PESO IDEAL')
elif 25 < imc <= 30:
    print(f'Seu IMC é de {imc} você esta com SOBREPESO')
elif 30 < imc <= 40:
    print(f'Seu IMC é de {imc} você esta OBESO')
else:
    print(f'Seu IMC é de {imc} você esta com OBESIDADE MÓRBIDA')
