# Programme qui demande a l'utilisateur le prix et la quantite d'un article
# ensuite calcule le sous-total, la taxe et le total a payer et les affiche

nom = input("Veuillez entrez le nom de l'article: ")
prix = float(input("Veuillez entrez le prix de l'article: "))
quantite = int(input("Veuillez entrez la quantite acheter: "))

# Calcule du sous-total
sous_total = prix * quantite

# Calcule de la taxe
taxe = sous_total * 0.13

# Calcule du total
total = sous_total + taxe

# Arrondir a 2 decimales
sous_total = round(sous_total, 2)
taxe = round(taxe, 2)
total = round(total, 2)

print("Le sous-total est de: " + str(sous_total) + " $")
print("La taxe est de: " + str(taxe) + " $")
print("Le total a payer est de: " + str(total) + " $")

print("Vous avez achete " + str(quantite) + " " + nom + " pour un total de " + str(total) + " $.")