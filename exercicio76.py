# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Régua', 3.50,
            'Canetas', 8.99,
            'Corretivo', 5.90,
            'Cola', 2.99)

for i in range(0, len(produtos), 2):
    print(f"{produtos[i]:.<15} R$ {produtos[i+1]:>3.2f}")