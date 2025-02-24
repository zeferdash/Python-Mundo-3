# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.
nums = (int(input("Digite um número: ")),
        int(input("Digite outro número: ")),
        int(input("Digite mais um número: ")),
        int(input("Digite o último número: ")))
print(f"Voce digitou os valores: {nums}")
print(f"O valor 9 apareceu {nums.count(9)} vezes.")
if 3 in nums:
    print("O número 3 apareceu nas seguintes posições:", end=" ")
    for i in range(len(nums)):
        if nums[i] == 3:
            print(i+1, end=" ")
else:
    print("O valor 3 não foi digitado.")
print()
print("Os valores pares digitados foram:", end=" ")
for n in nums:
    if n % 2 == 0:
        print(n, end=" ")