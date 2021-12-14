num1 = ""
num2 = ""
operador = ("")

print("Use a calculadora para fazer as seguintes operações: Soma = x+y, subtração = x-y, multiplicação = x*y, divisão = x/y ou exponeciação = x ^ y ou digite sair para parar")
while ("sair" not in num1 or num2):
    num1 = (input("digite o numero correspondente a x: "))
    if num1 == "sair":
        break
    operador = (input("digite um operador: (+ - * / ^): "))
    num2 = (input("digite o numero correspondente a y: "))
    if operador == "*":
        multi = float(num1) * float(num2)
        print(multi)
    if operador == "+":
        soma = float(num1) + float(num2)
        print(soma)
    if operador == "-":
        sub = float(num1) - float(num2)
        print(sub)
    if operador == "/":
        dividir = float(num1) / float(num2)
        print(dividir)
    if operador == "^":
        elevado = pow(float(num1), float(num2))
        print(elevado)
    