aviso = '''Esse programa vai te ajudar a calcular regra de 3
a estrutura vai ser exatamente assim:
num 1 <---> num 2
num 3 <---> x
ao preencher os 3 valores você terá o resultado de x, vamos começar?'''

print(aviso)

def regra_de_3(num1, num2, num3):
    resultado = (num2 * num3 / num1)
    return resultado

numero1 = float(input("digite o numero 1: "))
numero2 = float(input("digite o numero 2: "))
numero3 = float(input("digite o numero 3: "))
numero4 = regra_de_3(numero1, numero2, numero3)
resultado_limpo = round(numero4, 3)

print("", numero1, "<--->", numero2, "\n",numero3, "<--->", "x")
print("", numero2, "*", numero3, "=", numero1, "* x", "\n", 
numero2 * numero3, "/", numero1, "= x", "\n",
"x =", numero4)

print("O resultado da regra de 3 é: ", resultado_limpo)