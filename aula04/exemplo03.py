pontos = int(input('informe os pontos: '))

if pontos >= 100:
    pontos = pontos + 10
    print(f'Excelente! você tem {pontos} agora!')

if pontos >= 50:
    pontos = pontos + 5
    print(f'Bom! você tem {pontos} agora!')

else:
    print(f'voçê está no caminho certo! {pontos}')