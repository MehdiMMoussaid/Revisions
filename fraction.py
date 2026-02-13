#Mehdi Moussaid | 2/5/2026
#Programme qui donne la fraction simplifiée
#Import du bibilothecque math
import math as m

#Affichage du titre
titre = "Simplification d'une fraction "
millieu = "-"
print(f"{titre:<}")
print(f"{millieu:-<40}")

num = int(input("Entrez le numerateur de la fraction: "))
denom = int(input("Entre le denomninateur de votre fraction: "))

#Le function facteur permet le programme a determiner facilement le plus grande facteur commun. 
facteur = m.gcd(num, denom)

#Divise le numerateur et denominateur par le meme facteur pour calculer le nouveaux fraction simplifiée.
num = int(num/facteur)
denom = int(denom/facteur)

#Affiche le resultat.
print(f"La fraction simplifiée est {num} / {denom}")


