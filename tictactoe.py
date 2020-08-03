#-----------------------------Funciones-----------------------------
def estadoActual(posicion,jugador,juego):
	#Segun la eleccion del jugador posiciona el caracter en el...
	#lugar correspondiente
		juego = list(juego)
		if jugador == 1:
			juego[posicion - 1] = "O"
		elif jugador == 2:
			juego[posicion - 1] = "X"
		juego = tuple(juego)
		return juego

def checkWinner (juego):
	#Revisa si ya hay un ganador en el juego
	if juego[0] == juego[1] == juego[2] != " " or \
	juego[3] == juego[4] == juego[5] != " " or \
	juego[6] == juego[7] == juego[8] != " " or \
	juego[0] == juego[4] == juego[8] != " " or \
	juego[2] == juego[4] == juego[6] != " " or \
	juego[0] == juego[3] == juego[6] != " " or \
	juego[1] == juego[4] == juego[7] != " " or \
	juego[2] == juego[5] == juego[8] != " ":
		return True
	return False


juego=(" "," "," "," "," "," "," "," "," ")
i=0
numeros_escogidos=[]

while 1:

	try:
		posicion=int(input("Ingrese un numero de 1 a 9 para jugar \n"))
		if posicion<1 or posicion >9:
			print("El numero esta por fuera del rango")
			continue
	except:
		print("El valor ingresado no es valido")
		continue
	

	if posicion in numeros_escogidos:
		print("Ese lugar ya fue escogido")
		continue
	else:
		numeros_escogidos.append(posicion)


	if i % 2:
		jugador = 1
	else:
		jugador = 2
	i=i+1

	juego = estadoActual(posicion,jugador,juego)
	print(" %s | %s | %s \n __|___|__ \n %s | %s | %s \n __|___|__ \n %s | %s | %s" % juego)

	#Si ya hay un ganador o se produjo un empate, termina el juego
	if (checkWinner(juego)):
		if jugador == 1:
			print("El jugador 1 ha ganado \n El juego ha terminado")
		elif jugador == 2:
			print("El jugador 2 ha ganado \n El juego ha terminado")
		break
	if " " not in juego:
		print("Ha sido un empate \n El juego ha terminado")


