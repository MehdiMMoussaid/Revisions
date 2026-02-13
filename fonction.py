#Mehdi Moussaid | 2/6/2026
#Une programme qui calcule l'aire d'une carre, cercle et d'une rectangle

#Demande l'utilisateur pour enter leur formes qu'ils veule calculer l'aire de.
choix = input("Entrez le type de forme tu veux calculer l'aire (carre, cercle ou rectangle): ")

if (choix == "carre"):
    Longueur = float(input("Quelle est la longueur de votre carre: "))
    def aire_carre(Longueur):
        aire = Longueur**2
        return aire
    print(f"L'aire de votre carre c'est {aire_carre(Longueur)}")



if (choix == "cercle"):
    rayon = float(input("Quelle est le rayon de votre cercle: "))
    def aire_cercle(rayon):
        aire2 = 3.14 * rayon**2
        return aire2
    print(f"L'aire de votre cercle c'est {aire_cercle(rayon)}")


if (choix == "rectangle"):
    longueur = float(input("Quelle est le longueur de votre rectangle: "))
    largeur = float(input("Quelle est le largueur de votre rectangle: "))
    def aire_rectangle(longueur, largeur):
        aire = longueur * largeur
        return aire
    print(f"L'aire de ton rectangle c'est {aire_rectangle(longueur, largeur)}")

    


