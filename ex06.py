"""Ler um número inteiro N e calcular todos os seus divisores."""

N = int(input())

for i in range(1, N + 1):
    if N % i == 0:
        print(i)
