from datetime import datetime, date
from .models import *

def edad(list_):
    edad_list = []
    for fecha in list_:
        fecha_nacimiento = fecha.fn
        hoy = date.today()
        res = hoy - fecha_nacimiento #resto las fechas
        res2 = res / 365 #como devuelve en dias paso de dias a años
        stri = str(res2) #guardo el resultado como string 
        res3 = stri[0:2] #guardo solo los dos primeros caracteres de el resultado
        edad_list.append(res3)
    return edad_list
