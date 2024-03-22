salario = float(input('Informe o valor do seu salário: '))
if salario > 1250.00 :
    print('Com base no seu salário atual de R${:.2f}, consideramos um aumento de 10% na sua folha de pagamento. O seu novo salário é R${:.2f}.'.format(salario, ((salario * 10/100) + salario)))
else:
    print('Com base no seu salário atual de R${:.2f}, consideramos um aumento de 15% na sua folha de pagamento. O seu novo salário é R${:.2f}.'.format(salario, ((salario * 15/100) + salario)))
