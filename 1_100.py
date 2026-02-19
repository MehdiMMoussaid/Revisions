import random as r
#Mehdi Moussaid | Programme liste de nombres
#Un programme qui demande a l'utilisateur d'entrer des nombres entre 1 et 100
#Le programme arrete quand l'utilisateur entre le bonne nombre
#Ensuite il affiche plusieurs informations sur la liste

randnombre = r.randint(0,100)
print(randnombre)

#Fonction pour demander les nombres et remplir la liste

def demander_nombres():
    liste_nombres = []
    
    nombre = int(input("Entre un nombre entre 1 et 100: "))

    while nombre != randnombre:
        
        if nombre >= 1 and nombre <= 100:
            liste_nombres.append(nombre)
        else:
            print("Nombre invalide, reessaie.")
        
        nombre = int(input("Entre un nombre entre 1 et 100 (0 pour arreter): "))
    
    return liste_nombres


#Fonction pour calculer le nombre d'elements
def nombre_elements(liste):
    return len(liste)


#Fonction pour calculer la moyenne
def calcul_moyenne(liste):
    total = 0
    
    for n in liste:
        total = total + n
    
    if len(liste) > 0:
        moyenne = total / len(liste)
        return moyenne
    else:
        return 0


#Fonction pour compter les nombres pairs
def compter_pairs(liste):
    nb_pairs = 0

    for n in liste: 
        if n % 2 == 0:
            nb_pairs = nb_pairs + 1
    
    return nb_pairs


#Fonction pour compter les nombres impairs
def compter_impairs(liste):
    nb_impairs = 0
    
    for n in liste:
        if n % 2 != 0:
            nb_impairs = nb_impairs + 1
    
    return nb_impairs


#Fonction pour trouver le maximum (information au choix)
def trouver_max(liste):
    if len(liste) > 0:
        return max(liste)
    else:
        return 0

liste = demander_nombres()

print("Nombre d'elements:", nombre_elements(liste))
print("Moyenne:", calcul_moyenne(liste))
print("Nombre de nombres pairs:", compter_pairs(liste))
print("Nombre de nombres impairs:", compter_impairs(liste))
print("Maximum:", trouver_max(liste))