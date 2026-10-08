import subprocess 
subprocess.run("cls",shell=True)
from funciones import validador
lista=[]
apellido=input("Cual es tu apellido?\n")
año=int(input("En que año naciste??\n"))
altura=int(input("Cuanto medis??\n"))
lista.append(apellido)
lista.append(año)
lista.append(altura)
validador(lista)
final=validador(lista)
for i in range (len(final)):
    print(final[i])