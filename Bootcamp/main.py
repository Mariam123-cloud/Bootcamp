import random
print("Bienvenue! envie de faire une aventure? c'est parti!")
play=int(input("Tape 1 si tu veux jouer ! \n "))
if play == 1 :
    prénom=input("Quel est ton nom ?")
    print("\n")
    print("Salut", prénom)

from random import*
fichier = open("mots.txt")
liste_mots = fichier.readlines()    # met tous les mots du fichiers dans une liste
mot = choice(liste_mots)            # prend au hasard un mot dans la liste
mot = mot.rstrip()                  # supprime le caractère "saut à la ligne"
fichier.close()




tentatives = 6
point_erreur = 3
affichage = ""
lettres_trouvees = ""

for l in mot:
    affichage = affichage + "_ "

print(">> Bienvenue dans le jeu LET-GET <<")

print("################################")
print(">> vous avez 6 tentatives <<")
print("################################")
print(">> vous avez 3 points erreur<<")
print("################################")

n = int(input("veuillez choisir un niveau de 1 a 3 :  "))
print("vous avez choisi le niveau : ",n)

while tentatives > 0:
    print("\nMot à deviner : ", affichage)
    proposition = input("proposez une lettre : ")[0:1].lower()

    if proposition in mot:
        lettres_trouvees = lettres_trouvees + proposition
        print("-> Bien vu!")
    else:
        tentatives = tentatives - 1
        print("-> OUPS!lettre incorrecte\n")
        if tentatives == 0:
            print(" ==========Y= ")
        if tentatives <= 1:
            print(" ||/       |  ")
        if tentatives <= 2:
            print(" ||        0  ")
        if tentatives <= 3:
            print(" ||       /|\ ")
        if tentatives <= 4:
            print(" ||       /|  ")
        if tentatives <= 5:
            print("/||           ")
        if tentatives <= 6:
            print("==============\n")
            print("le nombre de tentatives restant est:",tentatives)
    affichage = ""
    for x in mot:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "

    if "_" not in affichage:
        print(">>> Gagné! \n Félicitations!vous avez devinez le mot<<<")
        break

print("\n    * Fin de la partie *   \n Oh Dommage! vous avez perdu ",prénom)

replay = int(input("Tape 1 pour rejouer, et sur 2 si tu veux quitter le jeu   "))
if replay !=1 :
    print("Aurevoir!")





