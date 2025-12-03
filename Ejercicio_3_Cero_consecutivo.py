#Este código recibirá una cantidad indefinida de números y, en caso de recibir dos 0 de manera consecutiva, regresará un True

def verificador_de_secuencia(*args):
  """
  Esta función recibirá los números ingresados por el usuario y virificará que no haya más de dos 0 de manera consecutiva.
  """
  resultado = False
  anterior = None
  
  for num in args:
    if num == anterior and num == 0:
      resultado =True
      break
    anterior = num
return resultado

solicitar_numeros = input('Ingresa la catidad de números que desees separados por espacios: ').split()
numeros = [int(n) for n in solicitar_numeros]
print(verificador_de_secuencia(*numeros))
