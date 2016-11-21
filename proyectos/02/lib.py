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
        


def cat(comando):#muestra el contenido de un archivo
	archivo=comando[1]
	dr=buscar(archivo)
	if dr==-1:
		print("Error archivo no encontrado")
		return False
	else:
		try:
			archivos=open(".archivos.file","r")
		except IOError:
			crearReq(1)
			archivos=open(".archivos.file","r")
		while dr[0]!="\\EOF":
			archivos.seek(int(dr[0]))
			print(archivos.read(int(dr[1])))
			dr=archivos.readline().split(" ")[0:2]#limite de tamano por parte 10**5
		archivos.close()

def hel(comando):
	os.system("cat help.txt")
	print("\n")

def crearReq(tipoError):
	if tipoError==0:
		cad="#esto es un comentario la tabla de archivos tiene 5 columnas\n#nombre		direccion	tamaño 		borrable\n"
		os.system("echo "+cad+" > .tablaDeArchivos.tbl")
	else:
		os.system("touch .archivos.file")
	# Esta funcion sirve para crear todos los requerimientos
	# antes de que otra funcion quiera operar


def tienePico(cmd):
	for i in cmd:
		if i==">>" or ">":
			return True
	return False

def buscar(archivo):
	#esta funcion busca un archivo en la tabla de
	#archivos y regresa su direccion en el archivo
	#de archivos, si no lo encuentra regresa -1
	try:
		tabla=open(".tablaDeArchivos.tbl","r")
	except IOError:
		crearReq(0)
		tabla=open(".tablaDeArchivos.tbl","r")
	for line in tabla:
		if line[0]!="#" and line[0]!="$":
			aux=line.split("\t")
			if aux[0]==archivo:
				tabla.close()
				return [aux[1],aux[2]]
	tabla.close()
	return -1

def buscarborrado():
	#esta funcion encuentra un archivo borrado para ser sustituido
	try:
		tabla=open(".tablaDeArchivos.tbl","r")
	except IOError:
		crearReq(0)
		tabla=open(".tablaDeArchivos.tbl","r")
	for line in tabla:
		if line[0]=="#":
			aux=tabla.tell()-len(line)
			tabla.close()
			return aux
	tabla.close()
	return -1



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
    #return 1;

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
                break
            if size >= 10 and size <= 99:
                table.seek(despT+21,0)
                table.write(str(size))
                break
            if size >= 100 and size <= 999:
                table.seek(despT+20,0)
                table.write(str(size))
                break
            if size >= 1000:
                table.seek(despT+19,0)
                table.write(str(size))
                break
        despT+=28
    table.close()
    
#Funcion agregar un archivo
def add(comando):
    global despN
    global actualSize
    Nombre = input()
    if len(Nombre)>10:
        print("Supera tamaño establecido")
        print("Presione enter para continuar")
    if len(Nombre)<=0:
        print("Ingrese un nombre")
        print("presione enter para continuar")
    texto = input()
    size = len(texto)

    if checkSize(size) == 1 and len(Nombre) <= 10 and len(Nombre)> 0:
        table=open("ejemploTabla.txt","r+")
        for line in table:
            aux=line.split("\t")
            if aux[0] == "0000000000":
                table.seek(despN,0)
                table.write(Nombre)
                despN += 28
                break
        direccion(size)
        blocksize(size)
        table.close()

despN = 0
tabla()

############################## Aqui acaba el acoplamiento de la tabla
