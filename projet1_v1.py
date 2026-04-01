import random as r
import time

# Mehdi Moussaid 03/10/2026 
# Mon programme est une application educatif qui permet l'utilisateur a jouer de jeux educatif 
# selon leur niveaux scolaires.

#Inialization du profile de l'eleve: 
def creationprofile(): 
    # demande le nom et le niveau de l'utilisateur
    nom = str(input("Nom: "))
    niveau = int(input("Niveau scolaire (1 a 6): "))
    return nom, niveau


def messageaccueil(nom, niveau):
    wait = 0.5
    time.sleep(wait)
    print("\n" + "="*50)
    print("BIENVENUE DANS L'APPLICATION ÉDUCATIVE")
    print("="*50)
    time.sleep(wait)
    print(f"\nBonjour {nom} !")
    time.sleep(wait)
    print(f"Tu es au niveau scolaire : {niveau}")
    time.sleep(wait)

    # message d'accueil pour expliquer l'application
    print("\nCette application a été conçue pour t'aider à apprendre")
    time.sleep(wait)
    print("et à pratiquer différentes matières scolaires en jouant.")
    time.sleep(wait)
    print("\nTu pourras choisir parmi plusieurs jeux éducatifs :")
    time.sleep(wait)
    print("\nLes jeux proposés changent selon ton niveau scolaire")
    time.sleep(wait)
    print("afin de te donner des exercices adaptés à ton âge.")
    time.sleep(wait)
    print("\nInstructions :")
    time.sleep(wait)
    print("1. Choisis un jeu dans le menu en entrant son numéro.")
    time.sleep(wait)
    print("2. Réponds aux questions en suivant les instructions à l'écran.")
    time.sleep(wait)
    print("3. Tu peux quitter l'application à tout moment en tapant 'q'.")
    time.sleep(wait)
    print("\nAmuse-toi bien et allons y!")
    input("(Tapez a pour proceder): ")

#Jeux pour les élèves de 1re et 2e année
#Jeux 1 (jeux de reorganiser une liste en ordre croissant)
def ordrecroissant():
    liste = []
    for i in range (5):
        liste.append(r.randint(0,50))
    print(f"Mettez cette liste en ordre croissant: {liste}")

    # tri par selection
    def triSelection(liste):   
        n = len(liste)
        # parcours toute la liste
        for i in range(n):
            minimum = i
            # cherche le plus petit element
            for j in range(i+1, n):
                if (liste[j] < liste[minimum]):
                    minimum = j
            # echange des valeurs
            temp = liste[i]
            liste[i] = liste[minimum]
            liste[minimum] = temp
        return liste

    reponse = []
    liste_tri = triSelection(liste)

    # l'utilisateur entre les nombres un par un
    while len(reponse) != len(liste_tri):
        reponse.append(int(input("Entrez ta reponse un nombre par la fois: "))) 
        print(f'Ta reponse: {reponse}')

    # verifie si la reponse est correcte
    if liste_tri == reponse:
        print("Tu a bien trier la liste!")
    else:
        print(f"Incorrect la bonne reponse est, {triSelection(liste.copy())} ")
    menu()

#jeux 2 (Combien de nombre pair/impair il y a dans une liste)
def nombrespairs():
    liste2 =[]
    for i in range (5):
        liste2.append(r.randint(0,20))
    print(liste2)
    
    numpair = int(input("Entrer le nombre de nombres pair il y a dans cette liste: "))
    numimpair = int(input("Entrer le nombre de nombre impair que'il y a das cette liste: "))
    
    n=0
    m=0

    # compte les pairs et impairs
    for i in liste2:
        x = i % 2
        if x == 0: 
            n = n+1
        else: 
            m = m+1

    # verifie les reponses
    if numpair == n and numimpair == m:
        print(f":) Bravo! tu a correctement compter les {n} nombres pairs et {m} nombres impairs dans cette liste!")
    elif numpair == n and numimpair != m:
        print(f":( Tu n'as pas bien compter les nombres impairs dans cette liste, il y avait {m} de nombres impairs.")
    elif numpair != n and numimpair == m:
        print(f":( Tu n'as pas bien compter les nombres pairs dans cette liste, il y avait {n} de nombres pairs.")
    elif numpair != n and numimpair != m:
        print(f":( Tu n'as pas bien compter les nombres impairs et pairs dans cette liste, il y avait {n} de nombres pairs et {m} de nombres impairs.")
    else:
        print("Une error sur notre cote c'est produite reasser de nouveaux!")
    menu()

#jeux 3 (Calcule mental)
def calculemental():
        a=0
        b=0

        # genere des nombres jusqu'a une condition
        while a + b < 20:
            a = r.randint(0,20)
            b = r.randint(0,20)
            op = r.choice(["+", "-"])

        # addition
        if op == "+":
            rep = a + b
            debut = time.time()
            userrep = input(f"Quelle est la somme de: {a} {op} {b} = ")
            fin = time.time()

        # soustraction
        else: 
            rep = a - b
            debut = time.time()
            userrep = int(input(f"Quelle est la difference entre: {a} {op} {b} = "))
            fin = time.time()

        print(rep)

        # verification
        if rep == userrep:
            print("Correct! En ", round(fin-debut,2),"secondes!")
        else:
            print("Mauvais reponse.")
        menu()

#jeux 4 (comparision de monnaie)
def comparision_monnaie():
    m1 = round(r.uniform(0.5,50), 2)
    m2 = round(r.uniform(0.5,50), 2)
    
    print("Quelle montant est la plus grande?:")
    print(f"1. : {m1}$ ou 2. : {m2}$")
    choix = int(input("Ta reponse: "))

    # verification du choix
    if (m1>m2 and choix == 1) or (m1<m2 and choix == 2):
        print("Correct!")
    else: 
        print("Incorrect. :(")
    menu()

#2eme a la 4eme annee

#Jeux 5 (determination des piece d'une montant de monnaie)
def piecesmonnaie():
    cent = r.randint(1, 5000)

    # Une fonction qui arrondis au plus proche 0.5
    def round_5(cent):
        return 5*round(cent/5) 

    # conversion en dollars
    cent = round_5(cent)
    dollars = float(cent / 100)

    print(f"Montant a rendre: {dollars}$")

    # saisie des pieces
    deux = int(input(f"Combien de pieces de 2$?: "))
    un = int(input(f"Combien de pieces de 1$?: "))
    c50 = int(input(f"Combien de pieces de 50¢?: "))
    c25 = int(input(f"Combien de pieces de 25¢?: "))
    c10 = int(input(f"Combien de pieces de 10¢?: "))
    c5 = int(input(f"Combien de pieces de 5¢?: "))

    # total donne par l'utilisateur
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

        # verification du montant
        if abs(dollars - total) < 0.0001:
            print("Le montant total est correct.")
        else:
            difference = round(dollars - total, 2)
            if difference > 0:
                print(f"Il manque {difference}$")
            else:
                print(f"Tu as donne {-difference}$ en trop.")

        # verification des pieces
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
    menu()
#Jeux 6 (calcule mental avancer)
def calculementalavancer():
        # generation des nombres pour calculs
        while a + b < 1000:
            a = r.randint(0,1000)
            b = r.randint(0,1000)
            op = r.choice(["+", "-"])

        # addition
        if op == "+":
            rep = a + b
            debut = time.time()
            userrep = input(f"Quelle est la somme de: {a} {op} {b} = ")
            fin = time.time()

        # soustraction
        else: 
            rep = a - b
            debut = time.time()
            userrep = int(input(f"Quelle est la difference entre: {a} {op} {b} = "))
            fin = time.time()

        print(rep)

        # verification
        if rep == userrep:
            print("Correct! En ", round(fin-debut,2),"secondes!")
        else:
            print("Mauvais reponse.")
        menu()

#Jeux 7 (Mots manquants)
def motsmanquants1():
    mot = "__________"
    phrase1, phrase2, phrase3 = ("Marco a " + mot + " un pomme.", 
                       "Anna a " + mot + " bonjour a son ami.", 
                       "Rico a " + mot + " pour le crayon.")
    randphrase = r.choice([phrase1, phrase2, phrase3])
    verbes = ["manger", "dit", "demander" ]
    
    print(f"{randphrase}\n Choisie le bon mot pour mettre dans la phrase:" )
    print(" ou ".join(verbes))
    rep = str(input("Ta reponse: "))

    # verification
    if (randphrase == phrase1 and rep == "manger") or \
   (randphrase == phrase2 and rep == "dit") or \
   (randphrase == phrase3 and rep == "demander"):
        print("Correct!")
    else: 
        print("Incorrect.")
    menu()

def motsmanquants2():
    mot = "__________"
    phrase1, phrase2, phrase3 = ("Plus tarde Gabriella " + mot + "a la plage.", 
                       "Mamadou " + mot + " le meme chandail que felix.", 
                       "Felix a " + mot + " aller au cinema avec ces amies, hier soir.")
    randphrase = r.choice([phrase1, phrase2, phrase3])
    verbes = ["vais", "veux", "pu" ]
    
    print(f"{randphrase}\n Choisie le bon mot pour mettre dans la phrase:" )
    print(" ou ".join(verbes))
    rep = str(input("Ta reponse: "))

    # verification
    if (randphrase == phrase1 and rep == "vais") or \
   (randphrase == phrase2 and rep == "veux") or \
   (randphrase == phrase3 and rep == "pu"):
        print("Correct!")
    else: 
        print("Incorrect.")
    menu()
    
def motsmanquants3():
    mot = "__________"
    phrase1, phrase2, phrase3 = ("Ils " + mot + " leurs efforts pour réussir malgré les difficultés.", 
                       "Nous " + mot + " attentivement les consignes pour éviter les erreurs.", 
                       "Tu " + mot + " tes idées clairement lors de la présentation.")
    randphrase = r.choice([phrase1, phrase2, phrase3])
    verbes = ["poursuivent", "lisons", "exprimes" ]
    
    print(f"{randphrase}\n Choisie le bon mot pour mettre dans la phrase:" )
    print(" ou ".join(verbes))
    rep = str(input("Ta reponse: "))

    # verification
    if (randphrase == phrase1 and rep == "poursuivent") or \
   (randphrase == phrase2 and rep == "lisons") or \
   (randphrase == phrase3 and rep == "exprimes"):
        print("Correct!")
    else: 
        print("Incorrect.")
    menu()

#Jeux 8 (tables de mutltiplication)
def tableauxdemultiplication():
    a = r.randint(1,10)
    b = r.randint(1,10)
    rep = int(input(f"{a} x {b} = "))

    def multiplication(a,b):
        if b == 0:
            return 0
        else: 
            return a + multiplication(a, b-1)

    if rep == multiplication(a, b): 
        print("Correct!")
    else: 
        print("Incorrect. La reponse etait, ", multiplication(a, b))
    menu()
   
#Jeux 9 (antonyme/synonym)
def jeuxsensdesmots():
    mots = {"heureux": ("joyeux", "triste"), "strict": ("rigide", "flexible"), "organisé": ("rangée", "désordre") }
    mot, (syn, ant) = r.choice(list(mots.items()))

    choix = r.choice(["synonym", "antonym"])
    print(f"Quelle est le {choix} de {mot}? (tapez 1 ou 2)")
    print(f"1. {syn} ou 2. {ant}")
    rep = int(input("Ta reponse: ") )

    # verification du type de reponse
    if choix == "synonym":
        if rep == 1: 
            print("Correct!")
        elif rep == 2: 
            print("Incorrect.")
        else:
            print("Une erreur c'est produite.")

    elif choix == "antonym": 
        if rep == 2: 
            print("Correct!")
        elif rep == 1: 
            print("Incorrect.")
    else: 
        print("Une erruer c'est produite.")
    menu()

    #Nouveaux jeux ajouter:

#Jeux 10 (Nombre manquant)
def nombre_manquant():
    a = r.randint(1,20)
    b = r.randint(1,20)
    c = a + b

    choix = r.choice(["a", "b"])

    if choix == "a":
        print(f"? + {b} = {c}")
        rep = int(input("Quel est le nombre manquant?: "))
        if rep == a:
            print("Correct!")
        else:
            print(f"Incorrect. La bonne reponse etait {a}")

    else:
        print(f"{a} + ? = {c}")
        rep = int(input("Quel est le nombre manquant?: "))
        if rep == b:
            print("Correct!")
        else:
            print(f"Incorrect. La bonne reponse etait {b}")
    menu()


#Jeux 11 (Suite logique)
def suite_logique():
    start = r.randint(1,10)
    step = r.randint(2,5)

    suite = [start, start+step, start+2*step]
    print(f"Complète la suite logique: {suite[0]}, {suite[1]}, {suite[2]}, ?")

    rep = int(input("Ta reponse: "))

    if rep == start + 3*step:
        print("Correct!")
    else:
        print(f"Incorrect. La bonne reponse etait {start + 3*step}")
    menu()


#Programme principale
def demarrer():
    global niveau
    choix = ""
    while choix != "oui":
        choix = input("Souhaite vous entrer dans l'application? (tapez oui ou non): ")
    nom, niveau = creationprofile()
    messageaccueil(nom, niveau)
    return (niveau, nom)
def menu():
    time.sleep(2)
    titre = " Menu "
    print(f"{titre:-^25}")
    if niveau >= 1 and niveau <= 2:
        print("1. Ordre croissant/decroissant\n2. Nombres Pairs/Impairs\n3. Calcule Mental\n4. Monnaie Canadien")

    if niveau >= 2 and niveau <= 4:
        print("5. Pieces de monnaie\n6. Calcule mental avancer\n7. Mots Manquantes")

    if niveau >= 3 and niveau <= 6:
        print("8. Tableaux de multiplication\n9.Synonym/Antonym")

    if niveau < 1 or niveau > 6:
        print("Error, Nombre invalid.")
    print("Jeux Extra:\n10. Nombre manquante\n 11.Suite logique")
    choix = input("Tapez le nombre du jeux pour jouer (ou q pour quiter): ")
    if choix == "1": ordrecroissant()
    elif choix == "2": nombrespairs()
    elif choix == "3": calculemental()
    elif choix == "4": comparision_monnaie()
    elif choix == "5": piecesmonnaie()
    elif choix == "6": calculementalavancer()
    elif choix == "7":
        if niveau <= 3:
            motsmanquants1()
        elif niveau <= 4:
            motsmanquants2()
        else:
            motsmanquants3()
    elif choix == "8": tableauxdemultiplication()
    elif choix == "9": jeuxsensdesmots()
    elif choix == "10": nombre_manquant()
    elif choix == "11": suite_logique()
    elif choix == "q": print("Au revoir!")
    else: print("Choix invalide")
    menu()
niveau, nom = demarrer()
menu()

