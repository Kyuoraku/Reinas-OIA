################
def menor(n, m):
	"""
	Devuelve el menor de los valores.

	Parámetros:
	n -- Se espera sea un valor entero.
	m -- Se espera sea un valor entero.

	"""
	if(n<=m):
		return n
	else:
		return m
############
def mayor(n,m):
	"""
	Devuelve el mayor de los valores.

	Parámetros:
	n -- Se espera sea un valor entero.
	m -- Se espera sea un valor entero.

	"""
	if(n>=m):
		return n
	return m
############
class Punto:
	"""
	Objeto que permite almacenar datos en forma de puntos.

	Atributos:

	x -- Se espera sea un valor entero.
	y -- Se espera sea un valor entero.


	"""
	x = 0
	y = 0

	def __init__(self, x = 0, y = 0):
		"""
		Inicializador, toma los argumentos dados y se los asigna al punto.
		Si no se da algún valor, se establece en 0.


		Argumentos:

		x -- Se espera sea un valor entero.
		y -- Se espera sea un valor entero.

		"""
		self.x = x
		self.y = y

	def cambiarPunto(self, x, y):
		"""
		Asigna una nueva coordenada al punto.

		Argumentos:
		x -- Se espera sea un valor entero.
		y -- Se espera sea un valor entero.

		"""
		self.x = x
		self.y = y
	def __str__(self):
		"""
		Devuelve una coordenada correspondiente a los atributos X e Y del punto.

		"""
		return "["+str(self.x)+";"+str(self.y)+"]"
##################################################
class Reina:
	"""
	Clase que permite almacenar los datos de las reinas.

	Atributos:
	numero_reina -- Se espera sea un valor entero. Es el número que representa a la reina ya que sus datos estaban en esa posicion del archivo de entrada.
	coordenadas -- Se espera sea un objeto de tipo Punto. Almacena las coordenadas de la reina sobre el tablero general.
	numero_conflictos -- Se espera sea un valor entero. Representa la cantidad de conflictos que se encuentran con respecto a las otras reinas y sus coordenadas.
	reinas_conflictos -- Se espera sea un array de enteros. Almacena los números de las reinas con las que se encuentra algún conflicto.

	"""
	numero_reina = 0
	coordenadas = Punto(0,0)
	numero_conflictos = 0
	#reinas_conflictos = []

	def __init__(self, coordenadas):
		self.numero_reina = 0
		self.coordenadas = coordenadas

	def setNReina(self, n):
		self.numero_reina = n

	def conflictoEncontrado(self):
		self.numero_conflictos += 1

	def conflictoConReinaN(self, n):
		if (int(n) != int(self.numero_reina)):
			if((self.reinas_conflictos.count(int(n)) < 1)):
				self.reinas_conflictos.append(n)

	def __str__(self):
		return "["+str(self.coordenadas.x)+";"+str(self.coordenadas.y)+"]"
##########################################################################
class Reinas:

	ruta=""
	reinas = []
	tablero = []

	def __init__ (self, ruta):
		"""
		Inicializador. Se hizo de esta forma para que no se tenga que ejecutar ninguno de los métodos de forma externa. Simplemente al darle a un objeto de tipo Reinas una cadena que represente la ruta del archivo de entrada, el problema se "resolverá solo".

		"""
		self.ruta = ruta
		self.ingresarInfo()
		self.cargarTablero()
		for i in range(len(self.tablero)):		#estas dos lineas muestran el tablero
			print(self.tablero[i])
		self.buscarXpositivo()
		self.buscarXnegativo()
		self.buscarYpositivo()
		self.buscarYnegativo()
		self.buscarDerechaArriba()
		self.buscarIzquierdaArriba()
		self.buscarDerechaAbajo()
		self.buscarIzquierdaAbajo()
		#for r in self.reinas:
		#	for i in r.reinas_conflictos:
		#		print(i)
		self.ordenarConflictos()
		pasar = str((self.__str__())) #aca estan puestos los datos de salida
		self.sacarDatos(pasar)

	def limpiar(self):
		self.ruta = ""
		self.reinas = 0
		self.tablero = []

	def ingresarInfo(self):
		"""
		Método que se encarga de extraer la información del .in y distribuirlo de acuerdo a la organización del programa.

		"""
		archivo = open(self.ruta)
		datos = archivo.readline();
		datos.split(" ")
		#print(datos[0]) #tamaño del tablero
		for i in range(int(datos[0])):
			self.tablero.append([0]*int(datos[0]))
		#self.reinas = []
		#for x in range(file_len("test0.in")-1):
		contador = 0
		for x in range(int(datos[2])):
			contador += 1
			linea = archivo.readline()
			linea.split(" ")
			equis = linea[0]
			ye = linea[2]
			puntoaux = Punto(equis,ye)
			aux = Reina(puntoaux)
			aux.setNReina(contador)
			aux.reinas_conflictos = []
			#falta ponerle el numero de reina.
			self.reinas.append(aux)
			#print(self.reinas[x]) #para ver si se cargan bien todas las reinas dentro del array.
		archivo.close()

	def cargarTablero(self):
		"""
		Método que se encarga de poner a cada reina donde corresponde en el tablero.

		"""
		for r in self.reinas:
			self.tablero[int(r.coordenadas.x)-1][int(r.coordenadas.y)-1] = int(r.numero_reina)
			#print(r.numero_reina)

	def ordenarConflictos(self):
		for r in self.reinas:
			r.reinas_conflictos.sort()

	def buscarXpositivo(self):
		"""
		Método que se encarga de buscar conflictos desde la posición actual de la reina dada, en dirección a valores de X crecientes.

		"""
		#print("Buscar X Positivo.")
		for r in self.reinas:
			#print("Coordenadas originales: "+str(r.coordenadas)) #coordenadas antes de ser modificadas
			aux = Punto(int(r.coordenadas.x) -1 ,int(r.coordenadas.y) -1) #le faltan los -1
			#print("Coordenadas tab: "+str(aux))
			for i in range(int(len(self.tablero)) - int(r.coordenadas.x)):
				#print("Tamaño del tablero: "+str(len(self.tablero)))
				if (int(aux.x) + 1 < len(self.tablero)):
					aux.x += 1
					#print("mod: "+str(aux)) #coordenadas despues de ser modificadas
				if(self.tablero[aux.x][aux.y] != 0):
					print("Conflicto de la "+str(r.numero_reina)+" reina con la "+str(self.tablero[aux.x][aux.y])+" reina en buscarXpositivo. VERIFICAR")
					if(self.tablero[aux.x][aux.y] != r.numero_reina):
						r.conflictoEncontrado()
						r.conflictoConReinaN(int(self.tablero[aux.x][aux.y]))
						break

	def buscarXnegativo(self):
		"""
		Método que se encarga de buscar conflictos desde la posición actual de la reina dada, en dirección a valores de X decrecientes.

		"""
		#print("Buscar X Negativo.")
		for r in self.reinas:
			#print("Coordenadas originales: "+str(r.coordenadas)) #coordenadas antes de ser modificadas
			aux = Punto(int(r.coordenadas.x) -1 ,int(r.coordenadas.y) -1) #le faltan los -1
			#print("Coordenadas tab: "+str(aux))
			for i in range(int(r.coordenadas.x)-1):			#PROBABLEMENTE ACA FALTA UN -1 PERO NO PUEDO PENSAR PORQUE ESTAN GRITANDO
				#print("Tamaño del tablero: "+str(len(self.tablero)))
				if (int(aux.x) - 1 >= 0):
					aux.x -= 1
					#print("mod: "+str(aux)) #coordenadas despues de ser modificadas
				if(self.tablero[aux.x][aux.y] != 0):
					if(self.tablero[aux.x][aux.y] != r.numero_reina):
						print("Conflicto de la "+str(r.numero_reina)+" reina con la "+str(self.tablero[aux.x][aux.y])+" reina en buscarXnegativo. VERIFICAR")
						if(self.tablero[aux.x][aux.y] != r.numero_reina):
							r.conflictoEncontrado()
							r.reinas_conflictos.append(int(self.tablero[aux.x][aux.y]))
							break

	def buscarYpositivo(self):
		"""
		Método que se encarga de buscar conflictos desde la posición actual de la reina dada, en dirección a valores de Y crecientes.

		"""
		#print("Buscar Y Positivo.")
		for r in self.reinas:
			#print("Coordenadas originales: "+str(r.coordenadas)) #coordenadas antes de ser modificadas
			aux = Punto(int(r.coordenadas.x) -1 ,int(r.coordenadas.y) -1) #le faltan los -1
			#print("Coordenadas tab: "+str(aux))
			for i in range(int(len(self.tablero)) - int(r.coordenadas.y)):
				#print("Tamaño del tablero: "+str(len(self.tablero)))
				if (int(aux.y) + 1 < len(self.tablero)):
					aux.y += 1
					#print("mod: "+str(aux)) #coordenadas despues de ser modificadas
				if(self.tablero[aux.x][aux.y] != 0):
					print("Conflicto de la "+str(r.numero_reina)+" reina con la "+str(self.tablero[aux.x][aux.y])+" reina en buscarXpositivo. VERIFICAR")
					if(self.tablero[aux.x][aux.y] != r.numero_reina):
						r.conflictoEncontrado()
						r.conflictoConReinaN(int(self.tablero[aux.x][aux.y]))
						break

	def buscarYnegativo(self):
		"""
		Método que se encarga de buscar conflictos desde la posición actual de la reina dada, en dirección a valores de Y decrecientes.

		"""
		#print("Buscar Y Negativo.")
		for r in self.reinas:
			#print("Coordenadas originales: "+str(r.coordenadas)) #coordenadas antes de ser modificadas
			aux = Punto(int(r.coordenadas.x) -1 ,int(r.coordenadas.y) -1)
			#print("Coordenadas tab: "+str(aux))
			for i in range(int(r.coordenadas.y)-1):			#PROBABLEMENTE ACA FALTA UN -1 PERO NO PUEDO PENSAR PORQUE ESTAN GRITANDO
				#print("Tamaño del tablero: "+str(len(self.tablero)))
				if (int(aux.y) - 1 >= 0):
					aux.y -= 1
					#print("mod: "+str(aux)) #coordenadas despues de ser modificadas
				if(self.tablero[aux.x][aux.y] != 0):
					if(self.tablero[aux.x][aux.y] != r.numero_reina):
						print("Conflicto de la "+str(r.numero_reina)+" reina con la "+str(self.tablero[aux.x][aux.y])+" reina en buscarYnegativo. VERIFICAR")
						if(self.tablero[aux.x][aux.y] != r.numero_reina):
							r.conflictoEncontrado()
							r.conflictoConReinaN(int(self.tablero[aux.x][aux.y]))
							break

	def buscarDerechaArriba(self):
		"""
		Método que se encarga de buscar conflictos desde la posición actual de la reina dada, en dirección a valores de X decrecientes y valores de Y crecientes, simultaneamente.

		"""
		#print("Buscar Derecha Arriba.")
		for r in self.reinas:
			#print("Coordenadas originales: "+str(r.coordenadas)) #coordenadas antes de ser modificadas
			aux = Punto(int(r.coordenadas.x) -1 ,int(r.coordenadas.y) -1) #le faltan los -1
			#print("Coordenadas tab: "+str(aux))

			#este es el momento en el que necesito una funcion que devuelva el numero mayor y el menor
			auxiliar = len(self.tablero) - (aux.y +1)
			for i in range(int(menor(aux.x, auxiliar))):
				#print("Tamaño del tablero: "+str(len(self.tablero)))
				aux.x -= 1
				aux.y += 1
				#print("mod: "+str(aux)) #coordenadas despues de ser modificadas
				if(self.tablero[aux.x][aux.y] != 0):
					print("Conflicto de la "+str(r.numero_reina)+" reina con la "+str(self.tablero[aux.x][aux.y])+" reina en buscarDerechaArriba. VERIFICAR")
					if(self.tablero[aux.x][aux.y] != r.numero_reina):
						r.conflictoEncontrado()
						r.conflictoConReinaN(int(self.tablero[aux.x][aux.y]))
						break

	def buscarIzquierdaArriba(self):
		"""
		Método que se encarga de buscar conflictos desde la posición actual de la reina dada, en dirección a valores de X e Y decrecientes, simultaneamente.

		"""
		#print("Buscar Izquierda Arriba.")
		for r in self.reinas:
			#print("Coordenadas originales: "+str(r.coordenadas)) #coordenadas antes de ser modificadas
			aux = Punto(int(r.coordenadas.x) -1 ,int(r.coordenadas.y) -1) #le faltan los -1
			#print("Coordenadas tab: "+str(aux))

			#este es el momento en el que necesito una funcion que devuelva el numero mayor y el menor
			for i in range(int(menor(aux.x, aux.y))):
				#print("Tamaño del tablero: "+str(len(self.tablero)))
				aux.x -= 1
				aux.y -= 1
				#print("mod: "+str(aux)) #coordenadas despues de ser modificadas
				if(self.tablero[aux.x][aux.y] != 0):
					print("Conflicto de la "+str(r.numero_reina)+" reina con la "+str(self.tablero[aux.x][aux.y])+" reina en buscarIzquierdaArriba. VERIFICAR")
					if(self.tablero[aux.x][aux.y] != r.numero_reina):
						r.conflictoEncontrado()
						r.conflictoConReinaN(int(self.tablero[aux.x][aux.y]))
						break

	def buscarDerechaAbajo(self):
		"""
		Método que se encarga de buscar conflictos desde la posición actual de la reina dada, en dirección a valores de X e Y crecientes, simultaneamente.

		"""
		#print("Buscar Derecha Abajo.")
		for r in self.reinas:
			#print("Coordenadas originales: "+str(r.coordenadas)) #coordenadas antes de ser modificadas
			aux = Punto(int(r.coordenadas.x) -1 ,int(r.coordenadas.y) -1) #le faltan los -1
			#print("Coordenadas tab: "+str(aux))

			#este es el momento en el que necesito una funcion que devuelva el numero mayor y el menor
			for i in range(int(len(self.tablero) - mayor(aux.x+1, aux.y+1))):
				#print("Tamaño del tablero: "+str(len(self.tablero)))

				aux.x += 1
				aux.y += 1
				#print("mod: "+str(aux)) #coordenadas despues de ser modificadas
				if(self.tablero[aux.x][aux.y] != 0):
					print("Conflicto de la "+str(r.numero_reina)+" reina con la "+str(self.tablero[aux.x][aux.y])+" reina en buscarDerechaAbajo. VERIFICAR")
					if(self.tablero[aux.x][aux.y] != r.numero_reina):
						r.conflictoEncontrado()
						r.conflictoConReinaN(int(self.tablero[aux.x][aux.y]))
						break

	def buscarIzquierdaAbajo(self):
		"""
		Método que se encarga de buscar conflictos desde la posición actual de la reina dada, en dirección a valores de X crecientes y valores de Y decrecientes, simultaneamente.

		"""
		#print("Buscar Izquierda Abajo.")
		for r in self.reinas:
			#print("Coordenadas originales: "+str(r.coordenadas)) #coordenadas antes de ser modificadas
			aux = Punto(int(r.coordenadas.x) -1 ,int(r.coordenadas.y) -1)
			#print("Coordenadas tab: "+str(aux))

			#este es el momento en el que necesito una funcion que devuelva el numero mayor y el menor
			auxiliar1 = len(self.tablero) - (aux.x +1)
			definitivo = menor(auxiliar1,aux.y)
			#print(definitivo) #cantidad de iteraciones posibles con los puntos adaptados al tablero
			for i in range(int(definitivo)):
				#print("Tamaño del tablero: "+str(len(self.tablero)))
				aux.x += 1
				aux.y -= 1
				#print("mod: "+str(aux)) #coordenadas despues de ser modificadas
				if(self.tablero[aux.x][aux.y] != 0):
					print("Conflicto de la "+str(r.numero_reina)+" reina con la "+str(self.tablero[aux.x][aux.y])+" reina en buscarIzquierdaAbajo. VERIFICAR")
					if(self.tablero[aux.x][aux.y] != r.numero_reina):
						r.conflictoEncontrado()
						r.conflictoConReinaN(int(self.tablero[aux.x][aux.y]))
						break

	def __str__(self):
		"""
		Método que se encarga de organizar los datos de salida.

		"""
		mostrar = ""

		flag = False
		for r in self.reinas:
			if (flag == False):
				mostrar+=str(r.numero_conflictos)
				mostrar+=" "
				flag = True
			else:
				mostrar+="\n"
				mostrar+=str(r.numero_conflictos)
				mostrar+=" "

			for i in r.reinas_conflictos:

				if (r.numero_reina == i):
					pass
				else:
					mostrar+=str(i)
					mostrar+=" "

		return mostrar;

	def sacarDatos(self, mostrar):
		"""
		Método que se encarga de escribir los datos de salida en un archivo externo.

		"""
		aux = self.ruta.split("/") #se corta la carpeta "entrada"
		aux2 = "salida/"+aux[-1] #se agrega la carpeta "salida"
		aux3 = aux2.split(".") #se corta la extension
		nuevaRuta = str(aux3[0])+".out" #se reemplaza por ".out"
			
		archivo = open(nuevaRuta, "w")
		archivo.write(str(mostrar))
		archivo.close()
###########################################################################################
#Nota mental: no ejecutar varios al mismo tiempo. Tira errores que no existen xd
#Primero = Reinas("entrada/test0.in")
#Segundo = Reinas("entrada/test1.in")
#Tercero = Reinas("entrada/test2.in")
#Cuarto = Reinas("entrada/test3.in")
#Quinto = Reinas("entrada/test4.in")
#Sexto = Reinas("entrada/test5.in")
#Septimo = Reinas("entrada/test6.in")