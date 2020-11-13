#MODULOS
import os, sys, time
from random import *

def corrida(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 250)

def valletta(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(2. / 120)

def saludo(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 100)

def medio(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(8. / 200)

def lento(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 200)

os.system("clear")

#---> INTERFAZ PRINECIPAL

corrida("\n       00000000            00         00        ")
corrida("      oo                   00         00        ")
corrida("     00          99    99   00       00   99999      ")
corrida("     00          99    99    00     00   pp   pp   ")
corrida("      oo         99    99     00   00    pp   pp   ")
corrida("       00000090   000000       00000      99999     ")
valletta("                                                   VALLETTA\n")

#---> SALUDO
saludo(" Hola! Soy tu asistente, que es lo que necesitas?")

#---> M E N U <----

print ("\n 1) MENSAJE PARA GIFT CARDS\n")
print (" 2) SALIR\n")
respuesta = int(input("Elige una respuesta: "))

# ============ OPCION 1 ==============

# - Preguntas -
if respuesta == 1:
        nombre = input("\n ¿Cual es el nombre de la victima? ")
        dni = input("\n ¿Cual es el DNI de la victima? ")
        ruc = input("\n ¿Cual es el RUC de la victima? ")
        domicilio = input("\n ¿Cual es el domicilio de la victima? ")

# ++- Mensaje -++

        print ("\n" + nombre + ", tenemos información personal suya, y tenemos la posibilidad de exponerlas si no hace caso a mis peticiones, solicito que usted compre una Gift Card de Google y me haga entrega del código, caso contrario, sus datos y sus cuentas serán hackeadas, expuestas y publicadas\n")

# ____ DNI ____

        if dni == "nose":
                dni = nulo

                if dni == nulo:
                        os.system("sleep 0")
        else:
                print ("DNI = " + dni)

# ___ RUC ____

        if ruc == "nose":
                ruc = nulo

                if ruc == nulo:
                        os.system("sleep 0")
        else:
                print ("RUC = " + ruc)

# ___ DOMICILIO ___

        if domicilio == "nose":
                domicilio = nulo

                if domicilio == nulo:
                        os.system("sleep 0")
        else:
                print ("DOMICILIO = " + domicilio)

# <-- COMPILACION DE DATOS -->

        nombreA = ("Nombres de la Victima: " + nombre)
        dniA = ("DNI de la victima: " + dni)
        rucA = ("RUC de la victima: " + ruc)

# ___ Crear Archivo ___

        medio("Logre recopilar la informacion que colocaste.")
        medio("Quieres que lo ponga en un archivo para que no lo pierdas?")
        print ("1) Si")
        print ("2) No")

        respuesta2 = input("Elige una Opcion: ")

# ___ Archivo ___


        if respuesta2 == "1":
                lento("CREANDO ARCHIVO...")

                archivo = open("archivo.txt","w")
                lento("Colocando datos...")

                archivo = open("archivo.txt","a")
                archivo.write("DATOS DE RECOPILACION\n")
                archivo.write("\n" + nombreA)
                archivo.write("\n" + dniA)
                archivo.write("\n" + rucA)

                medio ("En donde quieres guardar el archivo?")
                print ("       1) Ruta actual")
                print ("       2) Crear Carpeta 'victimas")
                print ("       3) Crear carpeta personalizada")
                print ("       4) Omitir")
                respuesta3 = input(" Elige una opcion: ")

# _________ RUTA ACTUAL _________

                if respuesta3 == "1":
                        print ("El archivo esta listo, si quieres verlo esta en tu ruta actual")

# __________ CREAR CARPETA VICTIMAS __________

                elif respuesta3 == "2":
                        lento("Creando carpeta nueva...")
                        os.system("mkdir victimas")
                        lento("Moviendo archivo...")
                        os.system("mv archivo.txt /data/data/com.termux/files/home/cuvo/victimas")

                        print ("El archivo esta listo, si quieres verlo esta en la carpeta victimas")

# __________ CREAR CARPETA PERSONALIZADA _____________

                elif respuesta3 == "3":
                        medio("Que nombre le quieres poner a la nueva carpeta")
                        respuesta4 = input("Coloca un nombre: ")
                        lento("Creando carpeta " + respuesta4 + "...")
                        os.system("mkdir " + respuesta4)
                        lento("Moviendo archivo...")
                        os.system("mv archivo.txt /data/data/com.termux/files/home/cuvo/" + respuesta4)

                        print ("El archivo esta listo, si quieres verlo esta en la carpeta" + respuesta4)

# __________ OMITIR __________

                elif respuesta3 == "4":
                        medio("Lo guardare en una ruta aleatoria")

                        aleatorio = ["actual","victimas"]
                        indice = randrange(len(aleatorio))
                        final = aleatorio[indice]

                        if final == "actual":
                                print ("El archivo esta listo, lo coloque en tu ruta actual")

                        elif final == "victimas":
                                os.system("mkdir victimas")
                                os.system("mv archivo.txt /data/data/com.termux/files/home/cuvo/victimas")
                                print (" El archivo esta listo, lo coloque en una nueva carpeta victimas")

# ____ OPCION NEGATIVA ____

        elif respuesta2 == "2":
                os.system("clear")

# ===============> OPCION 2 <=================

elif respuesta == 2:

# -- SALIDA --

        print ("Saliendo")
        os.system("clear")
        os.system("figlet VALLETTA")

# -- RESPUESTA INCORRECTA --

else:
        print ("ok")
        os.system("clear")
