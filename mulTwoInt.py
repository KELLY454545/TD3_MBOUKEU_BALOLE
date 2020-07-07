import sys

print(sys.argv)

if(len(sys.argv)==3):
    x = int(sys.argv[1])
    y =int(sys.argv[2])
    print(x+y)
elif(len(sys.argv)==2):
    x = int(sys.argv[1])
    y=(input("veuillez entree la troixieme valeur:  "))
    print(x+y)
elif(len(sys.argv)==1):
    x=(input("veuillez entree la deuxieme valeur: "))
    y=(input("veuillez entree la troixieme valeur: "))
    print(x+y)

else:
    print("erreur")
    







