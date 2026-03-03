'''
Boucle dans une liste
Vous pouvez parcourir les éléments
de la liste en utilisant une for boucle :
'''
thislist = ["apple", "banane", "cherry"]
for x in thislist:
    print(x)

'''
Vous pouvez également parcourir les éléments de la liste
en vous référant à leur numéro d'index.
Utilisez les fonctions range() et len() pour créer un itérable approprié.
'''
thislist = ["apple", "banane", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

'''
Utilisation d'une boucle While
Vous pouvez parcourir les éléments de la liste
en utilisant une while boucle.
Utilisez la len() fonction pour déterminer
la longueur de la liste,
puis commencez à 0 et parcourez les éléments de la liste
en vous référant à leurs index.
N'oubliez pas d'augmenter l'indice de 1 après chaque itération.
'''
thislist = ["apple", "banane", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# List Comprehension offre la syntaxe la plus courte pour parcourir les listes :
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
