
#Mehdi Moussaid || 02/23/2026

#Une fonction qui recherche une elements dans une liste:
def rechercheBinaire(liste, debut, fin, valeur): 
    if debut > fin:
        return False
    
    milleu = (debut+fin)//2
    
    if liste[milleu] == valeur:
        return True
    
    if valeur>liste[milleu]:
        return rechercheBinaire(liste, milleu + 1, fin, valeur)
    
    if valeur<liste[milleu]:
        return rechercheBinaire(liste, debut, milleu - 1, valeur)

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(rechercheBinaire(nombres, 0, len(nombres)-1, 6))
print(rechercheBinaire(nombres, 0, len(nombres)-1, 10))
