"""

AC2 - Aula do dia 30/08/2023

"""

# Cálculo de pagamento mensal

salario_hora = float(input('Salario: '))
horas_mes = float(input('horas mês: '))

def salario(salario_hora, horas_mes):
    return salario_hora * horas_mes
print(salario(salario_hora,horas_mes))

# Cálculo números

print("Cálculo de números!")

n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))
n3 = int(input("Escreva o terceiro número: "))

def numeros(numero_1,numero_2,numero_3):
    numero1 = numero_1*2*numero_2/2
    numero2 = numero_1*3 + numero_3
    numero3 = numero_3**3
    print(numero1,numero2,numero3)

numeros(n1,n2,n3)


# Cálculo números retornando

print("Cálculo de números retornando!")

n1_retornando = int(input("Escreva o primeiro número: "))
n2_retornando = int(input("Escreva o segundo número: "))
n3_retornando = int(input("Escreva o terceiro número: "))

def numeros_retornando(numero1_retornando,numero2_retornando,numero3_retornando):
    x = numero1_retornando*2*numero2_retornando/2
    y = numero1_retornando*3 + numero3_retornando
    z = numero3_retornando**3
    return x,y,z
print(numeros_retornando(n1_retornando,n2_retornando,n3_retornando))

# Cálculo ano bissexto

print("Cálculo ano bissexto!")

ano = int(input("Digite um ano:"))
def calcular_ano(a):
    bissexto = (a % 4 == 0) and (a % 100 != 0 or a % 400 == 0)
    print(f"{a} é bissexto: {bissexto}")

calcular_ano(ano)
