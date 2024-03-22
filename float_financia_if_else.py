valorcasa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacoes = valorcasa / (anos * 12)
print('Para pagar uma casa de R${:.0f} mil em {} anos,'.format(valorcasa, anos), end='')
print(' a prestação será de R${:.2f}.'.format(prestacoes))
if prestacoes <= 0.3 * sal:
    print('Empréstimo CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
