valor_original = float(input('informe o valor da compra (R$): '))

if valor_original >= 250:
    desconto = valor_original * 0.16
    valor_final = valor_original - desconto
    print(f'Você recebeu 16% de desconto! O valor final é R$ {valor_final:.2f}')

else:
    print(f'valor final da compra R$ {valor_original:.2f}')
    print(f'Você recebeu 16% de desconto! O valor final é R$ {valor_original:.2f}') 
