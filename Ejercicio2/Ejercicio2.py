#Get a list of files Ejercicio2/texto.txt
#• Process each file: Pista os.listdir():
#• 1. get size of each file
#file_stats = os.stat(file_name)
#print(file_stats)
#print(f'File Size in Bytes is {file_stats.st_size}')
#print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')
#• 2. count how many vowels(vocales) appear in the file. Pista: for loop
#• 3. Write the dictionary to a file Ejercicio2\resultados.txt (1 punto)
#The script should accept the number of threads to use required as user INPUT. (2 puntos)
#Make (2) thread safe using semaphores (2 puntos)

import threading
import time
import os


def countvocales():
    global vocales
    global lock
    with open(fichero) as f:
        for line in f:
            for char in line:
                if char in "aeiouAEIOU":
                    lock.acquire()
                    vocales += 1
                    lock.release()


def printvocales():
    global vocales
    global lock
    while True:
        lock.acquire()
        print("El fichero tiene", fichero,"tiene",vocales,"vocales")
        lock.release()
        time.sleep(1)

fichero = input("Introduce la ruta de tu fichero: ")

#fichero_size = os.path.getsize(fichero)
#print("El fichero", fichero, "tiene un tamaño de", fichero_size , "bytes")
file_stats = os.stat(fichero)
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')


vocales = 0
lock = threading.Lock()
t1 = threading.Thread(target=countvocales)
t2 = threading.Thread(target=printvocales)
t1.start()
t2.start()

t1.join()
t2.join()
