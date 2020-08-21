print("PostWrok 01 - Programa Pago Tarjeta")
print("Introduce la tasa de interés")
tasa_interes = float(input())
print("Introduce la cantidad de deuda")
deuda = float(input())
print("Introduce el pago a realizar")
pago = float(input())
print("Introduce los nuevos cargos")
cargos = float(input())
print("Tu Tasa de interes es:", tasa_interes)
print("Tu Deuda es de:", deuda)
print("El pago realizado es de:", pago)
print("Los nuevos cargos son:", cargos)
if pago > deuda:
    print("No es posible realizar pago superior al total de la deuda")
else:
    interes_mensual = (tasa_interes/12 )/100
    deuda_recalculada = (deuda - pago)*(1+interes_mensual)
    print("Deuda recalculada:", deuda_recalculada)
    nueva_deuda = deuda_recalculada + cargos
    print("El proximo cargo mensual es:", nueva_deuda)