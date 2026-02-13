#Programme qui demeande a l'utilisateur la longueur et largeur d'une rectangle et 
#ensuite calcule l'aire et permetre et l'affiche. 
longueur = int(input("Veuillez saisir la longueur de ton rectangle: "))
largeur = int(input("Veuillez saisir la largeur de ton rectangle: "))
unite = input("Veuillez entrez le type d'unite: ")

# Calcule du perimetre:
perimetre = (longueur + largeur)*2
# Calcule de l'aire: 
aire = longueur * largeur 

#Affichage
print("Le perimetre de ton rectangle mesure: " + str(perimetre) + " " + unite)
print("L'aire de ton rectangle est: " + str(aire) + " " + unite + "^2")