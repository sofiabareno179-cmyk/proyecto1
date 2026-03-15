def es_mayor_de_edad(edad:int)->bool:
 """ determinar si es mayor con bool"""
 if(edad>=18):
  return True # si es mayor a 18 seran true
 else:
  return False #si no es mayor dara false
#imprime si es TRUE o FALSE
edades:int=es_mayor_de_edad(20)
print(F"{edades}")
