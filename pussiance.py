#Calcule de la puissance: 
a = int(input("Quelle est la base: "))
b = int(input("Quelle est sa puissance: "))


def puissance(a,b):
    if b == 0: 
        return 1 
    else: 
        return a * puissance(a, b - 1) 
    
print(puissance(a,b))
        