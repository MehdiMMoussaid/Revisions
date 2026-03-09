#Mehdi Moussaid 3/9/2026
import random
import time 
liste = []

tempsDepart = time.time()

def listeHazard(quantite, min= 1, max=100):
    for i in range(quantite):
        liste.append(random.randint(min, max))
    return liste

liste_og = liste.copy()

def triSelection(liste, ordre="croissant"):
    if ordre == 1:
        ordre = "croissant"
    elif ordre == 2:
        ordre = "decroissant"
    
    n = len(liste)
    if ordre == "croissant":

  # Parcourir chaque élément de la liste
        for i in range(n):

     # Assume que le premier élément est le minimum
            minimum = i

     # Parcours la portion non triée pour trouver l’élément le plus petit
            for j in range(i+1, n):
            # vérifie si la position j contient l’élément le plus petit
                if (liste[j] < liste[minimum]):
                # Ajuste la position de l’élément le plus petit
                    minimum = j
            temp = liste[i]
            liste[i] = liste[minimum]
            liste[minimum] = temp

    elif ordre == "decroissant": 
        for i in range(n):
            minimum = i 
            for j in range (i+1, n):
                if (liste[j] > liste[minimum]):
                    minimum = j
     # Échange l’élément le plus petit avec l’élément au début de la portion non triée
            temp = liste[i]
            liste[i] = liste[minimum]
            liste[minimum] = temp

    return liste

#-^******* Programme Principale *******^-#
titre = " Tire une liste de nombre au hazard "
titre2 = " Dans quelle ordre veut tu trier la liste? "

print(f"{titre:*^40}")
quantite = int(input("Combien de nombres veut tu generer : "))
min = int(input("-- Plus petit nombre a generer : "))
max = int(input("-- Plus grand nombre a generer : "))
print(f"{titre2:*^50}\n")
print("1. Ordre croissant")
print("2. Ordre decroissant")
ordre = int(input("Choix (1 ou 2): \n"))
print(f"Voici la liste original: {listeHazard(quantite, min, max)}")
print(f"Voici la liste trier: {triSelection(liste, ordre)}")

tempsDepart = time.time()
nombresSelection = triSelection(liste.copy())
tempsSelecion = time.time() - tempsDepart

