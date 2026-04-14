#Exercice 2: 
# Créer un dictionnaire D qui associe à chaque mot d'une phrase sa longueur.

T = "Python est un langage de programmation polyvalent et facile à apprendre."

D = {}
for mot in T.split():
    D[mot] = len(mot)   
print(D)