#!/usr/bin/env python                                                     
# -*- coding: utf-8 -*-   
#esta es la biblioteca del micro sistema
import os
def impPresentacion():
	print("Micro sistema de archivos SanPer, creado por Max Armando Sanchez Hernandez y Perez Martinez David Antonio ")
	print("Escriba help para ayuda ")

def lsd(comando):
        try:
                table=open("ejemploTabla.txt","r")
        except IOError:
                crearReq(0)
                table=open("ejemploTabla.txt","r")
        for line in table:
                aux=line.split("\t")
                if aux[0]!="0000000000":
                        print(aux[0].strip('0')+"\t")
        table.close()

#Modifico la forma de borrar poniendo en ceros la el archivo a eliminar a eliminar
def dele(comando):
        nameDel = input()
        if len(nameDel) < 10:
                for i in range(len(nameDel),10):
                        nameDel += "0"
        
        despDel = 0
        fileNotFound = 0
        table=open("ejemploTabla.txt","r+")
        for line in table:
                aux = line.split("\t")
                if aux[0] == nameDel:
                   table.seek(despDel,0)
                   table.write("0000000000\t000\t000\t0000\t000\n")
                   fileNotFound = 1
                   break
                despDel+=28
        table.close()
        if fileNotFound == 0:
                print("El archivo no existe")
        

def buscar(archivo):
        tabla=open("ejemploTabla.txt","r")
        for line in tabla:
                aux=line.split("\t")
                if aux[0].strip('0')==archivo:
                        tabla.close()
                        return [aux[1],aux[2]]
                else:
                        return -1


def cat(comando):#muestra el contenido de un archivo
        archivo=comando[1]
        dr=buscar(archivo)
        if dr != -1:
                virtDisk = open("virtDisk.txt","r")
                for line in virtDisk:
                        aux = line.split("\t")
                        if aux[0] == dr[0]:
                                print(aux[1])
                                break
        else:
                print("archivo no encontrado")


def hel(comando):
        os.system("cat help.txt")
        print("\n")

################################### A partir de aqui acoplo nueva tabla


actualSize = 0

#Verifica el tamaño delarchivo
def checkSize(size):
    maxSize = 10000000
    global actualSize

    actualSize += size
    table=open("ejemploTabla.txt","r")
    for line in table:
        aux=line.split("\t")
        if aux[3]:
            if (actualSize+int(aux[3]))<=maxSize:
                actualSize+=int(aux[3])
                return 1
                break
        else:
                print("Espacio insuficiente para esa cadena")
                return 0
    table.close()

#tabla de archivos
def tabla():
    table=open("ejemploTabla.txt","w")
    #table.write("N\tDi\tDf\tT\tE\n")####################### N = Nombre, Di = Direccion de inicio, Df = Dirección final, T = tamaño, E = editado
    for x in range(0,10):
        table.write("0000000000\t000\t000\t0000\t000\n")
    table.close()

#almacena los datos del archivo #Aun por finalizar#
def disk(Nombre,texto):
    direccion=buscar(str(Nombre))
    almacen = open("virtDisk.txt","a+")
    table = open("ejemploTabla.txt","r")
    cadena = str(direccion)+"\t"+texto+"\n"
    almacen.write(cadena)
    table.close()
    almacen.close()

#Obtiene la direccion inicial y la direccion final
def direccion(size):
    global actualSize
    despDi = 11
    table=open("ejemploTabla.txt","r+")
    for line in table:
        aux=line.split("\t")
        if aux[1] == "000" and  aux[2] == "000":
##Se agrega cambio a desplazamiento de la direccion
            if actualSize-size <= 9:
                table.seek(despDi+2,0)
                tmp= actualSize-size
                table.write(str(tmp))
                break
            if actualSize-size<= 99 and actualSize-size >= 10:
                table.seek(despDi+1,0)
                tmp= actualSize-size
                table.write(str(tmp))
                break
            if actualSize-size > 99:
                table.seek(despDi,0)
                tmp= actualSize-size
                table.write(str(tmp))
                break
        else: despDi += 28
    table.seek(0,0)
    
    for line in table:
        aux=line.split("\t")
        if actualSize > 99:
                table.seek(despDi+4,0)
                table.write(str(actualSize))
                actualSize+=1
                break
        if actualSize >= 10 and actualSize <= 99:
                table.seek(despDi+5,0)
                table.write(str(actualSize))
                actualSize+=1
                break
        if actualSize <= 9:
                table.seek(despDi+6,0)
                table.write(str(actualSize))
                actualSize+=1
                break
    table.close() 

#pretende determinar el tamaño del bloque
def blocksize(size):
    despT = 0
    table=open("ejemploTabla.txt","r+")
    for line in table:
        aux=line.split("\t")
        if aux[3] == "0000" and aux[2] != "000":
            if size <= 9:
                table.seek(despT+22,0)
                table.write(str(size))
                table.close()
                break
            if size >= 10 and size <= 99:
                table.seek(despT+21,0)
                table.write(str(size))
                table.close()
                break
            if size >= 100 and size <= 999:
                table.seek(despT+20,0)
                table.write(str(size))
                table.close()
                break
            if size >= 1000:
                table.seek(despT+19,0)
                table.write(str(size))
                table.close()
                break
        despT+=28
    table.close()
    
#Funcion agregar un archivo
def add(comando):
    global despN
    global actualSize
    Nombre = input()
    Nombre = str(Nombre)

    if len(Nombre)>10:
        print("Supera tamaño establecido")
        print("Presione enter para continuar")
    if len(Nombre)<=0:
        print("Ingrese un nombre")
        print("presione enter para continuar")
    texto = input()
    size = len(texto)
    texto = str(texto)

    if checkSize(size) == 1 and len(Nombre) <= 10 and len(Nombre)> 0:
        table=open("ejemploTabla.txt","r+")
        for line in table:
            aux=line.split("\t")
            if aux[0] == "0000000000":
                table.seek(despN,0)
                table.write(Nombre)
                despN += 28
                break
        table.close()
        direccion(size)
        blocksize(size)
        disk(Nombre,texto)

despN = 0
tabla()

############################## Aqui acaba el acoplamiento de la tabla
