# Mehdi Moussaid || 02/26/2026
#Une programme qui decompose les multiplicaion 

# Fonction qui calcule le produit de deux nombres
def multiplier(a, b):

    # Étape de base : tout nombre multiplié par 0 donne 0
    if b == 0:
        return 0

    # fait a * b = a + a * (b - 1)
    else:
        return a + multiplier(a, b - 1)

# Demande à l'utilisateur d'entrer deux nombres
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))

# Calcul du produit à l’aide de la fonction récursive
resultat = multiplier(nombre1, nombre2)

# Affichage du résultat
print("Le produit de", nombre1, "et", nombre2, "est :", resultat)
