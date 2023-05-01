adicao = "+"
sub = "-"
divisao = "/"
multip = "*"

print("Escolha uma operação (+),(-),(/),(*)\n")
operador = input("Digite a operação que deseja:")

if(operador == adicao):
    valor1 = int(input("\nDigite o 1º número: "))
    valor2 = int(input("Digite o 2º número: "))
    res = valor1 + valor2
    print(f"A soma dos valores {valor1} e {valor2} é: {res}".upper())

elif(operador == sub):
    valor1 = int(input("\nDigite o 1º número: "))
    valor2 = int(input("Digite o 2º número: "))
    res = valor1 - valor2
    print(f"A Subtração dos valores {valor1} e {valor2} é: {res}".upper())

elif(operador == multip):
    valor1 = int(input("\nDigite o 1º número: "))
    valor2 = int(input("Digite o 2º número: "))
    res = valor1 * valor2
    print(f"A Multiplicação dos valores {valor1} e {valor2} é: {res}".upper())

elif(operador == divisao):
    valor1 = int(input("\nDigite o 1º número: "))
    valor2 = int(input("Digite o 2º número: "))
    res = valor1 / valor2
    print(f"A Multiplicação dos valores {valor1} e {valor2} é: {res}".upper())

else:
    print("\nPor gentileza digite um operador valido!!".upper())

"""
valor1 = int(input("ingrese el primer valor: "))
valor2 = int(input("ingrese el segundo valor: "))


resultado = valor1 + valor2
print(f"La suma de valores {valor1} y {valor2} és: {resultado}")
"""
