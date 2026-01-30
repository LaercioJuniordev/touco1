"""Fazer um programa para ler um número inteiro positivo N. O programa deve então mostrar na tela N linhas,
começando de 1 até N. Para cada linha, mostrar o número da linha, depois o quadrado e o cubo do valor, conforme
exemplo."""

N = int(input())

for i in range(1, N + 1):
    print(i, i**2, i**3)
