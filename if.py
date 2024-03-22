'''velocidade = float(input('Qual a velocidade do carro? '))
print('Dentro do limite de velocidade.' if velocidade <=80 else 'Será aplicada multa de R${:.2f} pelo fato do veículo estar acima do limite de velocidade.'.format((velocidade-80)*7))'''

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = ((velocidade - 80) * 7)
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')