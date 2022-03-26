# Receba o ano de nascimento e de acordo com sua idade calcule se ele ainda vai se alistar (quanto
# tempo ainda falta) se ele esta na idade já ou se já passou da idade (quanto tempo passou)

from datetime import date

nasc = int(input('Digite qual o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'Você possui {idade} anos')
sexo = int(input('Digite qual seu sexo, sendo:\n1 - Feminino\n2 - Masculino: '))

if sexo == 1:
    print('Você não precisa fazer o alistamento militar')
elif sexo == 2:
    if idade == 18:
        print('Você está na idade de fazer seu alistamento militar.')
    elif idade < 18:
        falta = 18 - idade
        print(f'Você ainda não esta na idade para fazer seu alistamento militar, faltam {falta} ano(s)')
        ano = atual + falta
        print(f'Você irá se alistar em {ano}')
    else:
        passou = idade - 18
        print(f'Você já tem idade para fazer seu alistamento militar, passou {passou} ano(s). FAÇA AGORA!')
        ano = atual - passou
        print(f'Você deveria ter se alistado em {ano}')
else:
    print('Opção de sexo inválida')

