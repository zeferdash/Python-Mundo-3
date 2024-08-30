nums = (int(input("Digite um número: ")),
        int(input("Digite outro número: ")),
        int(input("Digite mais um número: ")),
        int(input("Digite o último número: ")))
print(f"Voce digitou os valores: {nums}")
print(f"O valor 9 apareceu {nums.count(9)} vezes.")
if 3 in nums:
    print(f"O numero 3 apareceu na posicao: {nums.index(3)+1}")
else:
    print("O valor 3 nao foi digitado.")
print("Os valores pares digitados foram: ", end=" ")
for n in nums:
    if n % 2 == 0:
        print(n, end=" ")