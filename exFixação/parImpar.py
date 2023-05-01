"""
    Como descobrir se um número é impar ou par
"""

"""num = 5
numero = 2

print(num % numero)
"""

#variavel 
var_verifica = input("Digite um número: ")

# resto da variavel for igual a 0
var_resultado = int(var_verifica) % 2

#verifica se o resto da divisão é igual a 0
if var_resultado == 0:
    #se for apresenta a mensagem ao usúario
    print(f"O número digitado é par {var_verifica}")
else:
    #se não apresenta a mensagem dizendo que o número digitado é impar
    print(f"O número digitado é impar {var_verifica}")

