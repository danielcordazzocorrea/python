print('Verificadora de números perfeitos')
num = int(input('Coloque o número:  '))
lista = []
soma = 0
for a in range(1, num):
    if num % a == 0:
        lista.append(a)
for b in lista:
    soma += b
if soma == num:
    print(f'{num} é um número perfeito!')
else:
    print(f'{num} não é um número perfeito, a soma de seus divisores é {soma}')