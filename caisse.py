# Mehdi Moussaid | 02/09/2026 
# Une programme qui generer une montant d'argent et demenade a l'utilisateur 
# le nombre de chaque piece d'argent a fournis au client. 

# Importation du bibliotheque random qui permet de facile generer une nombre aleatoire
import random
titre = " Jeu De Monaie "
cent = random.randint(1, 5000)

# Une fonction qui arrondis au plus proche 0.5
def round_5(cent):
    return 5*round(cent/5) 

# On utilise la fonction puis converis en dollars
cent = round_5(cent)
dollars = float(cent / 100)

# Affchage du montant a rendre et le titre du programme. 
print(f"{titre:=^20}")
print(f"Montant a rendre: {dollars}$")

# Demande a l'utilisateur pour saisi le nombre de chaque type de pieces 
deux = int(input(f"Combien de pieces de 2$?: "))
un = int(input(f"Combien de pieces de 1$?: "))
c50 = int(input(f"Combien de pieces de 50¢?: "))
c25 = int(input(f"Combien de pieces de 25¢?: "))
c10 = int(input(f"Combien de pieces de 10¢?: "))
c5 = int(input(f"Combien de pieces de 5¢?: "))

# Determination du total
total = (deux*2) + (un*1) + (c50*0.5) + (c25*0.25) + (c10*0.10) + (c5*0.05)

def verify(dollars):

    reste = round(dollars, 2)

    piece2 = int(reste // 2)
    reste = round(reste % 2, 2)

    piece1 = int(reste // 1)
    reste = round(reste % 1, 2)

    piece50 = int(reste// 0.50)
    reste = round(reste % 0.50, 2)

    piece25 = int(reste // 0.25)
    reste = round(reste % 0.25, 2)

    piece10 = int(reste // 0.10)
    reste = round(reste % 0.10, 2)

    piece005 = int(round(reste / 0.05))

    print("----- Verification -----")

    # Verification du montant
    if abs(dollars - total) < 0.0001:
        print("Le montant total est correct.")
    else:
        difference = round(dollars - total, 2)
        if difference > 0:
            print(f"Il manque {difference}$")
        else:
            print(f"Tu as donne {-difference}$ en trop.")

    # Verification du nombre de pieces optimal puis affichage

    if (piece2 != deux):
        print(f"2$ Optimal: {piece2}")
    if (piece1 != un):
        print(f"1$ Optimal: {piece1}")
    if (piece50 != c50):
        print(f"50¢ Optimal: {piece50}")
    if (piece25 != c25):
        print(f"25¢ Optimal: {piece25}")
    if (piece10 != c10):
        print(f"10¢ Optimal: {piece10}")
    if (piece005 != c5):
        print(f"5¢ Optimal: {piece005}")
    else: 
        print("Les nombres de pieces sont optimal!")

verify(dollars)


