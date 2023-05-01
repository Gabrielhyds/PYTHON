"""
do while

Código para adivinhar um número.

"""
palpite = 0
numero = 9
# nos executamos sem verificar
while True:
    print("Qual o número correto? ")
    palpite = int(input())
# estamos verificando
    if palpite == numero:
        print("Parabéns você ACERTOU!\n")
        break
    else:
        print("Que pena você ERROU!\n")
else:
    print("Erro na aplicação!")
    print(bool(palpite))
