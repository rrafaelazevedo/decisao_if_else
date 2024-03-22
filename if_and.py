n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
# Verificando o número (nm) menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando o número (nm) maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}, já o outro extremo, isto é:número maior, foi {}.'.format(menor, maior))

'''n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
print('O maior número dos números digitados é {}.' .format(max(n1,n2,n3)))
print('O menor número dos números digitados é {}.'.format(min(n1,n2,n3)))'''
