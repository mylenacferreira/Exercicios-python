# Escreva um programa que leia a velocidade de um carro, se ele ulrapassar 80km/h escreva uma msg
# que ele foi multado e sua multa custa 7 reais por cada km acima do limite

vel = float(input('Digite qual a sua velocidade, em Km/h: '))

if vel > 80:
    print('Você está acima da velocidade e será MULTADO')
    cal = (vel - 80) * 7
    print(f'O valor da multa será de R${cal}')
print('Você não será multado, limite de velocidade aceitável.')
