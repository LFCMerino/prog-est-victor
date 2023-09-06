"""
AC 3 06/09/2023

"""
print("")
print("Calculadora salário")
print("")



def calculo_salario():

    salario_inicial = int(input("Escreva o seu salário: "))
    print(f"Salário antes do reajuste é {salario_inicial}")

    if salario_inicial <= 280:
        percentual = 0.2
    elif salario_inicial >= 280 and salario_inicial <= 700:
        percentual = 0.15
    elif salario_inicial >= 700 and salario_inicial <= 1500:
        percentual = 0.10
    elif salario_inicial >= 1500:
        percentual = 0.05
    else:
        print("Valor inválido!")

    resultado = salario_inicial *  percentual + salario_inicial
    aumento = salario_inicial * percentual

    print("Novo salário, após o aumento:", resultado)
    print("Percentual de aumento:", percentual)
    print("Valor do aumento:", aumento)


calculo_salario()

print("")
print("Cálculo dia da semana")
print("")

def dias(num):

     if num == 1:
          return "domingo"
     elif num == 2:
          return "segunda"
     elif num == 3:
          return "terça"
     elif num == 4:
          return "quarta"
     elif num == 5:
          return "quinta"
     elif num == 6:
          return "sexta"
     elif num == 7:
          return "sábado"
     else:
          return "inválido"
     
print(dias(5))

print("")
print("Calculadora Raiz quadrada")
print("")

def raiz():
    a = int(input("Escreva o valor de A:"))
    b = int(input("Escreva o valor de B:"))
    c = int(input("Escreva o valor de C:"))
    r = (b ** 2 - 4 * a * c)

    if a == 0:
        print("Inválido!")
    elif r < 0:
        print("A equação não possui raízes reais quando o delta é negativo.")
    else:
        print("O delta é positivo, então possui duas reaízes reais.")
        x1 = ((-b + r ** (1/2)) / (2 * a))
        x2 = ((-b - r ** (1/2)) / (2 * a))
        print("Respostas:\nx1 = ", x1, "\nx2 = ", x2)

raiz()       