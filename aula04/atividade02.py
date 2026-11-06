salario = float(input('informe o valor do salario (R$): '))
vendas = float(input('informe o valor das vendas (R$): '))
if vendas >= 1000: 
    bonus = 150
    salario_final = salario + bonus
    print(f'Você recebeu R$ {bonus:.2f} de bonus!')
    print(f'O valor final do seu salario é R$ {salario_final:.2f}')

elif vendas <= 500 and vendas < 1000:
    bonus = 75
    salario_final = salario + bonus
    print(f'Você recebeu R$ {bonus:.2f} de bonus!') 
    print(f'O valor final do seu salario é R$ {salario_final:.2f}')

else:
    print(f'Você não recebeu bonus!') 
    print(f'O valor final do seu salario é R$ {salario:.2f}')