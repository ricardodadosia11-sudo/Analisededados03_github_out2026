
valor_compra = float(input('Informe o valor da compra (R$): '))
cliente_fraquente = input('O cliente é frequente? (S/N): ').lower()[0]

if valor_compra > 100 or cliente_fraquente == 's':
    print('recebe o brinde')
else:
    print('não recebe o brinde')

  

