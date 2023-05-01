"""

Exercício - Trocar variáveis

"""
# trocando variaveis em python

x = input("Digite o valor de x: ")
y = input("Digite o valor de y: ")

# criaremos uma variavel temporaria

temp = x
x = y
y = temp

print(f"O valor de x depois da troca eh: {x}")
print(f"O valor de y depois da troca eh: {y}")
