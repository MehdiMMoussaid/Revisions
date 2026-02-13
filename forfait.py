# Programme : Forfait téléphonique
# Ce programme calcule le cout mensuel selon les donnees mobiles utiliser

# Demande a l'utilisateur la quantite de donnees utiliser
donnees = float(input("Veuillez entrer la quantite de donnees utiliser (en Go): "))

# Structure de decision pour determiner le prix
if donnees >= 0 and donnees <= 5:
    cout = 30
elif donnees > 5 and donnees <= 10:
    cout = 45
elif donnees > 10 and donnees <= 20:
    cout = 65
else:
    cout = 90

# Affiche le montant a payer
print(f"Le montant a payer est de {cout} $")

# Message d'avertissement si la consommation depasse 15 Go
if donnees > 15:
    print("Attention: votre consommation depasse 15 Go ")