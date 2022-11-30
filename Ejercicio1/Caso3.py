#Implementa en python un código de Productor Consumidor mediante cola sincronizada tal que:
#-El productor produce números enteros mayor que 10 y menor que 1000, el productor produce
#10 números cada vez que los almacena en la cola y el tiempo de espera entre 
#la generación de un número y otro es de PT segundos (1 punto)
#Prueba el algoritmo con los distintos casos usando una relación de productor:consumidor de
#2:10 con PT=1  CT=10 y X=4 (0,5 puntos)
#El consumidor lee X números de la cola de golpe, calcula el MCD de esos X números .(1,5 punto)
#el tiempo de espera entre la lectura de X elementos cola y la siguiente lectura de 
# los siguientes X elementos es de  CT segundos (1 punto)
#el tiempo de espera entre la lectura de X elementos de la cola y la siguiente lectura de 
# los siguientes X elementos es de  CT segundos (1 punto)


import random
import time
import threading
import math
import queue

#Variables globales
PT=1
CT=10
X=4
cola=queue.Queue()
lock=threading.Lock()

#Funcion productor
def productor():
    while True:
        time.sleep(PT)
        for i in range(10):
            num=random.randint(10,1000)
            print("Productor produce: ",num)
            cola.put(num)

#Funcion consumidor
def consumidor():
    while True:
        time.sleep(CT)
        numeros=[]
        for i in range(X):
            numeros.append(cola.get())
        print("Consumidor consume: ",numeros)
        cola.task_done()
        lock.acquire()
        print("MCD: ",mcd(numeros))
        lock.release()

#Funcion principal
def main():
    #Creamos los hilos
    hilo1=threading.Thread(target=productor)
    hilo2=threading.Thread(target=consumidor)
    #Iniciamos los hilos
    hilo1.start()
    hilo2.start()
    #Esperamos a que los hilos terminen
    hilo1.join()
    hilo2.join()

#Funcion para calcular el MCD
def mcd(numeros):
    mcd=numeros[0]
    for i in range(1,len(numeros)):
        mcd=math.gcd(mcd,numeros[i])
    return mcd

if __name__ == "__main__":
    main()