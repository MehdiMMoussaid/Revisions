#Mehdi Moussaid || 02/13/2026
import random

# Fonction qui retourne la valeur maximale d'une liste
def maxListe(liste):
    maximum = liste[0]  # On commence avec le premier élément dans le liste
    for i in liste:
        if i > maximum:
            maximum = i
    return maximum


# Fonction qui retourne la somme des éléments d'une liste
def sommeListe(liste):
    somme = 0
    for element in liste:
        somme = somme + element
    return somme


# Fonction qui retourne la moyenne des éléments d'une liste
def moyenneListe(liste):
    somme = sommeListe(liste)  # On réutilise la fonction somme
    moyenne = somme / len(liste)
    return moyenne

# Création d'une liste de nombres au hasard
liste = []

for i in range(10):
    nombre = random.randint(1, 100)
    liste.append(nombre)

print("Voici la liste :", liste)

# Appel des fonctions
print("Valeur maximale :", maxListe(liste))
print("Somme des éléments :", sommeListe(liste))
print("Moyenne des éléments :", moyenneListe(liste))