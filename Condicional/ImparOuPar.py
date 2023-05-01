"""
    programa que calcula se o número digitado é par ou impar

"""

var_num = input("Digite um número: ");

var_result = int(var_num) % 2;

if(var_result == 1):
    print(f"esse numero é impar")
elif(var_result == 0):
    print(f"Esse número é par")