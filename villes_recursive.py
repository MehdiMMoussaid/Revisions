
#Mehdi Moussaid || 02/23/2026

#Une fonction qui recherche une elements dans une liste:
def rechercheLineaire(liste, pos, valeur): 
    if pos >= len(liste):
        return False
    if liste[pos] == valeur:
        return True
    return rechercheLineaire(liste, pos+1, valeur)

villes = ["Ottawa", "Toronto", "Sudbury"]
print(rechercheLineaire(villes, 0, "Toronto"))
print(rechercheLineaire(villes, 0 , "Wawa"))