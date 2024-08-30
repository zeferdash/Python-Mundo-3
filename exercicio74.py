# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

numeros = tuple(random.randint(1, 100) for n in range(5))  # Gera 5 números aleatórios entre 1 e 100

print("Números sorteados:", numeros)
print("Menor número:", min(numeros))
print("Maior número:", max(numeros))

