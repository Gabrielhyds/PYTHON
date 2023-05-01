# maiúsculas e minúsculas
# símbolos e espaços

"""
security = chave
5ecurt1ty = senha

hexadecimal.

1 = 1
2 = 2
3 = 3
4 = 4
5 = 5
6 = 6
7 = 7
8 = 8
9 = 9
10 - 9 = A
11 - 9 = B
12 - 9 = C
13 - 9 = D
14 - 9 = E
15 - 9 = F
16 - 9 = G
17 - 9 = H
18 - 9 = I
19 - 19= J

@ = K
# = L
$ = M
% = N
& = O
* = P
( = Q
) = R
- = S
+ = T
_ = U
. = V
/ = W
ª = X
º = Y
? = Z
"""

chave = input("Digita a base da sua senha: ")

senha = ""

for letra in chave:
    if letra in "Aa":
        senha += "1"

    elif letra in "Bb":
        senha += "@"

    elif letra in "Cc":
        senha += "3"

    elif letra in "Ee":
        senha += "4"

    elif letra in "Ff":
        senha += "5"

    elif letra in "Ss":
        senha += "%"

    elif letra in "Rr":
        senha += "#"

    elif letra in "Mm":
        senha += "$"

    else:
        senha += letra
print(senha)
