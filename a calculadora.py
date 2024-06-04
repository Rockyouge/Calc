from calculadora import calculadora

n1 = float(input("Diga um número: "))
n2 = float(input("Diga mais um número: "))
print("operações: somar, subtrair, multiplicar")

op = input("Escreva o nome da operação desejada: ")

calc = calculadora()

if op == "somar":
    print(calc.somar(n1, n2))
elif op == "subtrair":
    print(calc.subtrair(n1, n2))
elif op == "multiplicar":
    print(calc.multiplicar(n1, n2))
else:
    print("Operação inválida")

