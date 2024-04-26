import logging
import time

def calcular_suma_parcial(inicio, fin):
    logging.info(f'Función con rango: {inicio} - {fin}')
    suma = 0
    for i in range(inicio, fin + 1):
        suma += i
        time.sleep(0.01)
    return suma
