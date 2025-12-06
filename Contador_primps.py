#Este programa recibirá un número (rango máximo) y contará todos los números primos que se encuentren dentro de ese rango.
#Este conteo va desde el 0 hasta el número incluído, pero el 0 y el 1 no se consideran como primos.

def es_primo(numero):
   if numero <= 1: #Eliminamos el 0 y 1 porque no son primos
      return False
   for i in range(2, int(numero**0.5) + 1): #buscamos si el número tiene otro divisor además de él mismo y el 1
      if numero % i == 0: #si el divisor no deja un residuo (un decimal) entonces el número no es primo
         return False
   return True

def contar_primos(limite):
  contador = 0

  for num in range(2, limite + 1): 
     if es_primo(num):
        contador += 1
  return contador

limite = int(input('Ingresa el límite hasta el que hay que contar: '))
cantidad = contar_primos(limite)
print(f'Desde el 0 hasta el {limite} hay {cantidad} números primos.')
