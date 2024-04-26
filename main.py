from lib import *
import pandas as pd
import logging
import time
from concurrent.futures import ThreadPoolExecutor

nombre_archivo = input('Nombre del archivo:')
df = pd.read_excel(nombre_archivo, index_col=False)

array = df.values.flatten().tolist()
print(len(array))

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

while True:
    try:
        num_hilos = int(input("¿Cuántos hilos quiere crear?: "))
        if 2 <= num_hilos <= 10:
            break
        else:
            print("Error: La cantidad de hilos debe estar entre 2 y 10.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

t0 = time.time()

globalArrayNum1 = [array]
def contadorDos(inicio, fin):
    logging.info(f'Función con rango: {inicio} - {fin}')
    for i in range(inicio, fin+1, 1):
        globalArrayNum1.append(i)
        time.sleep(0.01)
    return 0
t0 = time.time()

globalArrayNum = []
with ThreadPoolExecutor(max_workers=num_hilos) as executor:
    inicio = 1
    fin = 10000
    subrango = fin // num_hilos
    for i in range(inicio, num_hilos + 1):
        intento = subrango * i
        globalArrayNum.append(executor.submit(calcular_suma_parcial, inicio, intento))
        inicio = subrango + inicio

sumas_parciales = [result.result() for result in globalArrayNum]
suma_total = sum(sumas_parciales)

tf = time.time() - t0
print(globalArrayNum1)
print("Sumas parciales:", sumas_parciales)
print("Suma total:", suma_total)
print(f'Tiempo de ejecución: {tf} ')