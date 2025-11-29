#Este código recibirá 3 integers como parámetros, los sumará y, dependiendo del resultado, mostrará un valor diferente.
#Si la suma de los 3 números es mayor a 15, devolverá el número mayor.
#Si es menor a 10, devolverá el menor.
#Si el resultado está entre 10 y 15 (ambos números incluídos), devolverá el valor medio.

def devolver_distintos(*args):

    resultado = sum(args)
    if len(args) != 3:
        return "Error: Se deben proporcionar exactamente 3 números enteros."
    else:
        if resultado > 15:
            return max(args)
        elif resultado < 10:
            return min(args)
        else:
            return sorted(args)[1]
    
args = input("Introduce 3 números enteros separados por espacios: ").split()
args = [int(num) for num in args]
print(devolver_distintos(*args))