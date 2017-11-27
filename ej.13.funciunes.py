#!/usr/bin/env python
# -*- coding: utf-8
def crealista(lista):
	if numero < 1:
		print "Imposible!!"
	else:
		lista=[]
		for i in range(0,numero):
			print "Digame un numero"
			num=int(input())
			lista+=num
		print "La lista creada es:", lista
		lista=[]
		
def sumalista(lista):
	suma=0
	for i in lista:
		suma+=i
		print "La suma de la lista es:", suma
		
print "Digame un numero:"
numero=int(input())
lista=[]
crealista(lista)
sumalisa(lista)
