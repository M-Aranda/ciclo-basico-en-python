"""
Compila
"""

from time import sleep


cont=0
while(True):
    print("Progresando...")
    cont+=1
    sleep(30)
    print("Progreso al",cont,"%")
    print("...prosiguiendo")
    if(cont==100):
        break
