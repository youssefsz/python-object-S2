#Execice1 : 
# ecrire un programe qui process un chaine de caractere et creation dun dict qui a code de chaque caractere et le nombre de fois qu'il apparait dans la chaine

T = "Python est un langage de programmation polyvalent et facile à apprendre."
D = {}
for c in T:
    D[c] = T.count(c)
print(D)