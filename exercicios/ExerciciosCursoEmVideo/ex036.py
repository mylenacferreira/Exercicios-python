# pergunte o valor da casa, do salario e quantos anos voce vai pagar. Calcule o valor mensal sabendo que
# ela nao pode exceder 30% do salario se não será negado

valor = float(input('Qual é o valor da casa que você deseja financiar?: R$ '))
salario = float(input('Qual é o valor do seu salário atualmente?: R$'))
anos = int(input('Em quantos anos você pretende pagar por essa casa: '))
parcela = (valor / anos) / 12  # valor que terá que pagar MENSALMENTE
teste = (salario * 0.3)  # Verifica qual é o valor que corresponde a 30% do salário
print(f'Parcela mensal R${parcela:.2f} e 30% do salario corresponde a R${teste:.2f}')
if parcela >= teste:
    print(f'EMPRÉSTIMO NEGADO.')
else:
    print(f'EMPRÉSTIMO CONCEDIDO.')