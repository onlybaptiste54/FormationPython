import sys

Course = []

while True:  
    menu = """\n1: Ajoute un élément à ta liste
2: Retire un élément de ta liste
3: Affiche la liste
4: Vider la liste
5: Quitter
"""
    choix = input(menu + "Votre choix : ")

    if not choix.isdigit() or not (1 <= int(choix) <= 5):
        print("Choix invalide, essayez encore.")
        continue  
    
    choix = int(choix)  

    if choix == 1:
        element = input("Quel élément ajouter à la liste ? ")
        Course.append(element)  
        print(f"L'élément '{element}' a été ajouté à la liste.")
    elif choix == 2:
        element = input("Quel élément retirer de la liste ? ")
        if element in Course:
            Course.remove(element)  
            print(f"L'élément '{element}' a été retiré.")
        else:
            print(f"L'élément '{element}' n'est pas dans la liste.")
    elif choix == 3:
        print("Voici ta liste :", Course)

    elif choix == 4:
        Course.clear()  
        print("La liste a été vidée.")
    elif choix == 5:
        print("Au revoir !")
        sys.exit()  
