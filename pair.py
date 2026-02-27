#Mehdi Moussaid || 02/23/2026
#Une programme qui utilise la recursivite pour determiner
#si une nombre entrez par l'tilisateur est pair une impair

print(f"Determinons si ton nombre est pair ou impair")
n = int(input("Veuillez saisir ton nombre: "))

#Fonction qui determine si une nombre est pair 
#en utilisant la recursivite 
def pair(n): 
    if n == 1:
        return False
    elif n == 0: 
        return True
    else: 
        return pair(n-2)
pair(n)

#Affichage du resultat
if pair(n) == False : 
    print(f"Ton nombre n'est pas pair.")
elif pair(n) == True : 
    print(f"Ton nombre est pair.")
    

