# Gere uma calculadora simples com verificações de if operador == + num1 + num2
# para realizar calculos simples. a calculadora deve suportar adicao, subtracao
# divisao e multiplicao. a calculadora deve conter tratamentos de erros simples,
# como por exemplo nao aceitar um numero no input de operador.

def calculadora():
    num1 = float(input("Insira o primeiro número: "))
    operador = input("Insira o operador (+, -, *, /): ")
    num2 = float(input("Insira o segundo número: "))
    
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Erro: Operador inválido. Por favor, use +, -, * ou /."
    
    return f"O resultado de {num1} {operador} {num2} é: {resultado}"

print(calculadora())