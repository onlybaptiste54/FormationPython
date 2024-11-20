import random
NombreAléatoire = random.randint(0,100)




for i in range (1,6):
    Question = int(input("Quel est le nombre mystère ? "))
    
    if Question >NombreAléatoire:
        print("C'est en dessous! réessaye "+ str(NombreAléatoire))
    elif Question<NombreAléatoire:
        print("C'est au dessus! réessaye de "+str(NombreAléatoire))
    else:
        print("bien joué!tu a réussi en seulement:"+str(i)+"essaies")
        break
    
    if i==5:
        print("Dommage tu n'as plus d'essaies!Le nonmbre était:"+str(NombreAléatoire))
