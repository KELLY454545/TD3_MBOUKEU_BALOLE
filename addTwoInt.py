import sys
<<<<<<< HEAD
=======

def add(a,b):
	return a+b

if __name__ == "__main__":

	print(sys.argv)

	if(len(sys.argv)==3):
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		print(add(x,y))

	elif(len(sys.argv)==2):
		y=(input("veuillez entree la deuxieme valeur:"))
		x= int(sys.argv[1])
		print(add(x,y))

	elif(len(sys.argv)==1):
		x=(input("veuillez entree la deuxieme valeur:"))
		y=(input("veuillez entree la troisieme  valeur:"))
		print(add(x,y))

	else:
		print("Erreur")
>>>>>>> 39a9148a9abfef1329ce2eb0fe87910c4524068d

def add(a,b):
	return(int(a+b))

if __name__ == "__main__":

	print(sys.argv)

	if(len(sys.argv)==3):
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		print(add(x,y))

	elif(len(sys.argv)==2):
		y=int(input("veuillez entree la deuxieme valeur:"))
		x= int(sys.argv[1])
		print(add(x,y))

	elif(len(sys.argv)==1):
		x=int(input("veuillez entree la deuxieme valeur:"))
		y=int(input("veuillez entree la troisieme  valeur:"))
		print(add(x,y))

	else:
		print("Erreur")


