
#Mehdi Moussaid || 02/23/2026

def afficheRecursif(n, pos):
    if pos >= len(n): 
        return
    
    print(n[pos])
    return afficheRecursif(n, pos+1)

nombres = [7,2,1,5,3,0]
print(afficheRecursif(nombres, 0))