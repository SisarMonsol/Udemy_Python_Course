#Este código recibirá una cantidad indefinida de números y, en caso de recibir dos 0 de manera consecutiva, regresará un True

def verificador_de_secuencia(*args):
  """
  Esta función recibirá los números ingresados por el usuario y virificará que no haya más de dos 0 de manera consecutiva.
  """
  resultado = False
  for num in args:
    
  
  return resultado

numeros = input('Ingresa la catidad de números que desees: ')
print(verificador_de_secuencia(numeros))
