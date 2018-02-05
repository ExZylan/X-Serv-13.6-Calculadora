#!/usr/bin/python3

import sys

if len(sys.argv) == 4:
	try:
		if sys.argv[1] == "sumar":
			print (float(sys.argv[2]) + float(sys.argv[3]))
		if sys.argv[1] == "restar":
			print (float(sys.argv[2]) - float(sys.argv[3]))
		if sys.argv[1] == "multiplicar":
			print (float(sys.argv[2]) * float(sys.argv[3]))
		try:
			if sys.argv[1] == "dividir":
				print (float(sys.argv[2]) / float(sys.argv[3]))
		except ZeroDivisionError:
			print("no puedes dividir por 0")
	except ValueError:
		print("Utilizar numero enteros o reales")
else:
	print ("Utilizar: funcion operando1 operando2")