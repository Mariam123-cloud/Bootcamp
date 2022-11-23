import random
#Ce document contient les reponses des questions 2 et 3.

#Commentaire de specifications
#Bibliotheque de fonction

def saisieniveau():
    """
    objectif:choisir son niveau de jeu de 1 a 3.

    methode:utilisation d une boucle avec des instrutions sequentielles.

    besoins:nombre(n),variable i.

    entrees:-

    connus:choix du niveau de jeu,le nombre de lettre du mot proposé.

    sortie:-

    resultats:le niveau choisi,le nombre de mots du niveau chargés

    hypothese:1<nombre3


    """

    tentatives = 6
    points_erreurs=3

    while n > 0 and n <= 3:
        n, i = int(input("veuillez choisir un niveau de 1 a 3")),
        i = n
        int(input("vous avez choisi le niveau", i))


    def saisielettre(lettres_trouvees,proposition,tentatives,mot ):

        """
        objectif:saisir des lettres pour former le mot a deviner.

        methode:utilisation d une boucle avec des instrutions sequentielles.

        besoins:lettre(l),temps(t),lettres_trouvees,proposition,tentatives,solution.

        entrees:les lettres du mot qu on doit saisir.

        connus:-

        sortie:le nombre de  tentatives restantes et le nombre de  tentatives perdues,avertissements.

        resultats:savoir si on a perdu ou gagner et voir le mot secret.

        hypothese:tentataive>0,si proposition se trouve dans le mot.


       """

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
                    print("le nombre de tentatives restant est:", tentatives)


    def affichage(lettres_trouvees,mot):
        """
        objectif:affichage du mot secret et savoir si on a gagné ou perdu.

        methode:utilisation d une boucle avec des instrutions sequentielles.

        besoins:lettres_trouvees,solution.

        entrees:-

        connus:niveau.

        sortie:le score obtenu et le plus grand score.

        resultats:affichage du mot secret.

        hypothese:-

        """

        affichage = ""
        for x in mot:
            if x in lettres_trouvees:
                affichage += x + " "
            else:
                affichage += "_ "

        if "_" not in affichage:
            print(">>> Gagné! \n Félicitations!vous avez devinez le mot<<<")
            breakpoint()

    print("\n    * Fin de la partie *   \n Dommage! vous avez perdu.")
