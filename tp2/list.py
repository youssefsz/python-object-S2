L1 = ["apple", "banana", "cherry"]
L2 = [10, 20, 30, 40]
print(type(L1))
print(type(L2))

#Modifier la 2 et 3 eme valeur en les remplacant par une seul
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:3] = ["melon"]
print(thislist)

#Inserer 'Pasteque' comme 3 element
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "pasteque")
print(thislist)

#exemple
thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "orange")
print(thislist)

#Ajouter Liste dans un Liste
L1 = ["apple", "banana", "cherry"]
L2 = ["mango", "poire", "peche"]
L1.extend(L2)
print(L1)

#Ajouter n'importe quel objet(tuples,dic,etc)
L1 = ["apple", "banana", "cherry"]
L2 = ("mango", "poire")
L1.extend(L2)
print(L1)

#Remove the item
L1 = ["apple", "banana", "cherry"]
L1.remove("banana")
print(L1)

#supprimper index specifié - pop(1)
L1 = ["apple", "banana", "cherry"]
L1.pop(1)
print(L1)

#supprimper le dernier element - pop()
L1 = ["apple", "banana", "cherry"]
L1.pop()
print(L1)

#Supprimer l'element a l'index 0 - del
L1 = ["apple", "banana", "cherry"]
del L1[0]
print(L1)

#Supprimer toute la liste - del
L1 = ["apple", "banana", "cherry"]
del L1
# print(L1) # This would raise NameError as L1 no longer exists

#effacer le contenu de la liste - clear()
L1 = ["apple", "banana", "cherry"]
L1.clear()
print(L1)
