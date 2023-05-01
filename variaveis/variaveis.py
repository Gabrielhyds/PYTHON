x = 5
# x recebe o valor 5
y = 3.5
z = 1+2j

W = "Gabriel"
w = 'Gabriel'

# A-z , 0-9 e _
# altura , Altura e ALTURA são variaveis diferentes

h = 10
j = 12
q = 34
print(h)
print(j)
print(q)

a = b = c = " faz o curso de Python3"
print(a)
print(b)
print(c)

h = w + a
print(h)

q = x + j
print(q)
# retorna um erro porque não se pode concatenar um texto e um número.
# aqui fica claro que o python é uma tipagem dinâmica e forte.
q = w + x
print(q)
