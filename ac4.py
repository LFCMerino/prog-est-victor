"""
AC 4
13/09/2023

"""

print("")
print("Cálculo número primo!")
print("")

def e_primo(num):
    primo = True
    for div in range(2, num):
        if num % div == 0:
            print(div)
            primo = False
    if primo == True:
        print("É primo")
    else:
        print("O número não é primo.")

e_primo(6)

print("")
print("Cálculo de parcelas!")
print("")

def parcelas_divida():
    valor = int(input("Escreva o valor: "))
    parcelas = int(input("Escreva quantas vezes deseja parcelar: "))

    if parcelas >= 3:
        porcentagem = 0.10
    elif parcelas >= 6:
        porcentagem = 0.15
    elif parcelas >= 9:
        porcentagem = 0.20
    elif parcelas <= 12:
        porcentagem = 0.25
    else:
        print("Quantidade de parcelas acima do limite.")
    
    resultado = valor * porcentagem + valor
    valor_parcela = valor / parcelas

    print("Valor Inicial:", valor)
    print("Valor dos juros:", porcentagem)
    print("Valor da dívida:", resultado)
    print("Quantidade de parcelas:", parcelas)
    print("Valor da parcela:", valor_parcela)

parcelas_divida()