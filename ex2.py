"""Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando
essas informações conforme exemplo (use a palavra "in" para dentro do intervalo, e "out" para fora do intervalo)"""

N = int(input())

dentro = 0
fora = 0

for _ in range(N):
    x = int(input())
    if 10 <= x <= 20:
        dentro += 1
    else:
        fora += 1

print(f"{dentro} in")
print(f"{fora} out")
