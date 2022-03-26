# Receba o valor de salario de um funcionário e calcule seu aumento
# Para salarios maiores 1250 -> 10% e para inferiores ou iguais -> 15%

salario = float(input('Informe o seu salário: R$ '))

if salario > 1250:
    atual = salario * 1.1
else:
    atual = salario * 1.15
print(f'O seu salario atual será de R${atual}')
