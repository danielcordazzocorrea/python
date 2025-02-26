#Você coloca quantos números primos você quer ver e ele mostra dentro de uma lista
cont = 0
lista = []
conta = 0
n = int(input('Quantos números primos você quer ver?  '))
while True:
    cont += 1
    for a in range(1, cont):
        if cont % a == 0:
            conta += 1
    if conta == 1:
        lista.append(cont)
    conta = 0
    if len(lista) == n:
        break
print(lista)