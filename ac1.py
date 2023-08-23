print("Calculadora de equação do segundo grau!")
print("")
print("Equação utilizada: ax² + bx + c = 0")
print("")
a = int(input("Escreva o valor de A:"))
b = int(input("Escreva o valor de B:"))
c = int(input("Escreva o valor de C:"))

r = (b ** 2 - 4 * a * c)
x1 = ((-b + r ** (1/2)) / (2 * a))
x2 = ((-b - r ** (1/2)) / (2 * a))

print("Respostas:\nx1 = ", x1, "\nx2 = ", x2)

# Ano bissexto

ano = int(input("Digite um ano:"))
bissexto = (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)
print(f"{ano} é bissexto: {bissexto}")