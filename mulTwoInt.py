import sys

def mul(a,b):
	return a*b

if __name__=="__main__":

	print(sys.argv)

	if(len(sys.argv)==3):
    		x = int(sys.argv[1])
    		y =int(sys.argv[2])
    		print(mul(x,y))
	elif(len(sys.argv)==2):
    		x = int(sys.argv[1])
    		y=(input("veuillez entree la troixieme valeur:  "))
    		print(mul(x,y))

	elif(len(sys.argv)==1):
    		x=(input("veuillez entree la deuxieme valeur: "))
    		y=(input("veuillez entree la troixieme valeur: "))
    		print(mul(x,y))
	else:
    		print("erreur")
    







