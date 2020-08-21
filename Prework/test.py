"""print("Introduce el primer numero")
num1 = int(input())
print("Introduce el segundo numero")
num2 = int(input())
suma = num1 + num2
resta = num1 - num2
modulo = num1%num2
print("La suma es", suma)
print("La resta es", resta)
print("El modulo es", modulo)"""

"""
print("Introduce numero a multiplicar")
num3 = int(input())
for x in range(1,11):
    msj = " {} X {} =  {}"
    print(msj.format(num3, x, str(num3 * x)))
"""

"""
print("Que deseas de topping?")
topping = input()
if (topping == "oreo"):
    print("El precio es", 19)
elif (topping == "m&m"):
    print("El precio es", 25)
elif (topping == "fresas"):
    print("El precio es", 22)
elif (topping == "brownie"):
    print("El precio es", 28)
else:
    print("el producto no esta disponible")
"""

print("Introduce el primer numero")
num1 = int(input())
print("Introduce el segundo numero")
num2 = int(input())   
print("Selecciona la operación a realizar")
operacion = input()
if (operacion == "+"):
    resultado = num1 + num2
    print("Resultado", resultado)
elif (operacion == "-"):
    resultado = num1 - num2
    print("Resultado", resultado)
elif (operacion == "*"):
    resultado = num1 * num2
    print("Resultado", resultado)
elif (operacion == "/"):
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado", resultado)
elif (operacion == "%"):
    resultado = num1 % num2
    print("Resultado", resultado)
else:
    print("Operación no valida")
