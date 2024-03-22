n = int(input('Digite um valor pra verificarmos se o mesmo é par, ou ímpar: '))
resultado = n % 2
if resultado == 0:
    print('O número {} é PAR, pois o quociente de {}/2 resulta 0.'.format(n, n))
else:
    print('O número {} é ÍMPAR, pois o quociente de {}/2, resulta 1.'.format(n, n))