print("\n-----------------------------------------------------")
print("Separador de pares e ímpares\n")

numeros = input("Insira alguns números separados por espaço para \nque eu possa separar os pares dos ímpares\n\n:-) -> ").split( )

pares = []
impares = []

for numero in numeros:
	if int(numero)%2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)

print ("\nNumeros pares: %s"  %(pares))
print ("Numeros impares: %s"  %(impares))