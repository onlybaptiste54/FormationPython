from ast import While
import random
import sys

LifeEnemie = 50
LifeHeros = 50

AttaqueEnemie = random.randint(5,15)
AttaqueHero = random.randint(5,10)
Potion = 3
Vierendu = random.randint(15,50)



while LifeEnemie > 0 and LifeHeros > 0:
    print(f"Il vous reste{LifeHeros} pv ")
    user_choice = ""
    while user_choice not in [1, 2]:
        user_choice = int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "))

    if user_choice == 1:
        AttaqueHero = random.randint(5,10)
        LifeEnemie -=AttaqueHero

        AttaqueEnemie = random.randint(5,15)
        LifeHeros -= AttaqueEnemie
        print(f"Vous infligez {AttaqueHero} points de dégâts à l'ennemi.")
        print(f"L'ennemi vous inflige {AttaqueEnemie} points de dégâts.\n")
    elif user_choice == 2 and Potion > 0:
        AttaqueEnemie = random.randint(5,15)
        VieRendue = random.randint(15, 50)  # Récupérer des points de vie aléatoires
        Potion -=1
        LifeHeros += Vierendu
        print(f"Vous utilisez une potion et récupérez {VieRendue} points de vie.")

        LifeHeros -= AttaqueEnemie
        print(f"L'ennemi vous inflige {AttaqueEnemie} points de dégâts.\n")
    elif user_choice == 2 and Potion == 0:
        print("Vous n'avez plus de potions !\n")
    else:
        print("Choix invalide, essayez encore.\n")
        


if LifeEnemie <=0 and LifeHeros>0:
    print("Bien joué tu a vaincu l'enemie")
else:
    print("loser")