"""
lista = ["Sergio", "Ivan", "Francisco", "Alex", "Omar"]
print(lista)
lista.sort()
print(lista)
lista.append("Zapata")
lista.sort()
print(lista)
"""
"""
directorio = {"Alan" : "1222", "Javier": "26855"}
print(directorio["Alan"])
directorio["Sergio"] = "5555"
print(directorio)
"""

memoria ={}
def calcular_fibonacci(n:int) -> int:
    if n== 1:
        return 1
    if n== 0:
        return 0
    if n in memoria:
        return memoria[n]
    memoria[n] = calcular_fibonacci(n-1) + calcular_fibonacci(n-2)
    return  memoria[n]

def mcm(x : int, y : int, z : int) :
    maximo = max([x,y,z])
    while True:
        if maximo % x == 0 and maximo % y == 0 and maximo % z == 0:
            res = maximo
            break
        maximo += 1
    return res
   
if __name__ == '__main__':
    #for i in range (10):
    #    print(calcular_fibonacci(i))
    res = mcm(2, 10, 3)
    print(res)
