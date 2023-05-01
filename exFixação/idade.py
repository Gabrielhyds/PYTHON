"""
01 - Implemente um programa que receba a idade de uma pessoa e imprima
mensagem de acordo com os critérios:
    ● Menor de 16 anos: MENOR
    ● Entre 16 e 18 anos: EMANCIPADO
    ● Maior de 18 anos: MAIOR

"""
idade = int(input("Digite sua idade"))
if idade < 16:
    print("MENOR")
if idade >= 16:
    if idade < 18:
        print("EMANCIPADO")
    elif idade >= 18:
        print("MAIOR")
