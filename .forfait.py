#Forfait telephonique 
#Une programme qui determine le montant a paye selon les donnes en Go utiliser: 
#Demande a l'utilisateur le nombre de donnes en Go utiliser pendant le mois: 
titre = " Calculons ton forfait "
print(f"{titre:+^50}")
go = float(input("Le nombre de donnees utiliser cette mois (en Go ): "))

#Code qui determiner le montant a paye selon le nombre de donnees utiliser
if (go>0 and go<=5): 
    cout = "30$"
elif (go>5 and go<=10): 
    cout = "45$"
elif (go>10 and go<=20): 
    cout = "65$"
elif (go>20): 
    cout = "90$"
else: 
    print("Error")

#Affiche le montant a paye: 
print(f"Vous avez utiliser {go} de donnes cette mois-ci donc, vouz doivez: {cout}")

if go > 15:
    print(f"Attention ton usage depasse 15 go.")