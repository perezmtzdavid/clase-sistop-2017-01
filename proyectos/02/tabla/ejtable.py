#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
import sys

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
                break
            else:
                print("Espacio insuficiente para esa cadena")
                return 0
    table.close()
    return 1;

#tabla de archivos
def tabla():
    table=open("ejemploTabla.txt","w")
    #table.write("N\tDi\tDf\tT\tE\n")####################### N = Nombre, Di = Direccion de inicio, Df = Dirección final, T = tamaño, E = editado
    for x in range(0,10):
        table.write("0000000000\t000\t000\t0000\t000\n")
    table.close()

#almacena los datos del archivo #Aun por finalizar#
def disk(newElement):
    almacen=open("virtDisk.txt","w")
    almacen.close()
    
#Obtiene la direccion inicial y la direccion final
def direccion(size):
    global actualSize
    despDi = 11
    #despDf = 15
    table=open("ejemploTabla.txt","r+")
    for line in table:
        aux=line.split("\t")
        if aux[1] == "000" and  aux[2] == "000":
            table.seek(despDi,0)
            tmp= actualSize-size
            table.write(str(tmp))
            break
        else: despDi += 28
    table.seek(0,0)
    
    for line in table:
        aux=line.split("\t")
        table.seek(despDi+4,0)
        table.write(str(actualSize))
        break
    table.close()

#pretende determinar el tamaño del bloque
def blocksize(size):
    despT = 0
    table=open("ejemploTabla.txt","r+")
    for line in table:
        aux=line.split("\t")
        if aux[3] == "0000" and aux[2] != "000":
            table.seek(19,0)
            table.write(str(size))
            #despT += 28
            break
    table.close()

    
#Funcion agregar un archivo
def add():
    global despN
    global actualSize
    Nombre = input()
    if len(Nombre)>10:
        print("Supera tamaño establecido")
    if len(Nombre)<=0:
        print("Ingrese un nombre")
    
    texto = input()
    size = len(texto)

    if checkSize(size) == 1:
        table=open("ejemploTabla.txt","r+")
        for line in table:
            aux=line.split("\t")
            if aux[0] == "0000000000":
                table.seek(despN,0)
                table.write(Nombre)
                despN += 28
                break
                
    direccion(size)
#    blocksize(size)
    table.close()

    Nombre = input()

    if checkSize(size) == 1:
        table=open("ejemploTabla.txt","r+")
        for line in table:
            aux=line.split("\t")
            if aux[0] == "0000000000":
                table.seek(despN,0)
                table.write(Nombre)
                despN +=28
                break
    table.close()

    direccion(size)
    Nombre = input()

    if checkSize(size) == 1:
        table=open("ejemploTabla.txt","r+")
        for line in table:
            aux=line.split("\t")
            if aux[0] == "0000000000":
                table.seek(despN,0)
                table.write(Nombre)
                despN +=28
                break
    table.close()
    
    direccion(size)

despN = 0
tabla()
add()
