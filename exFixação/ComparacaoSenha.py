senha = int(input("Digite sua senha: ".upper()))
contraSenha = int(input("Confirme sua senha: ".upper()))

if senha == contraSenha:
    print("\nSenhas iguais!".upper())
else:
    print("Senhas diferentes!".upper())
