# TP5 : Les ensembles (set) en Python
# Ce programme est uniquement a but educatif.

print("Parcourir un ensemble et imprimer les valeurs :")
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

print(sep="\n")
print(sep="\n")
print(sep="\n")


print("Ajouter un element avec add() :")
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
print(sep="\n")
print(sep="\n")
print(sep="\n")


print("Ajouter un ensemble avec update() :")
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
print(sep="\n")
print(sep="\n")
print(sep="\n")


print("Ajouter n'importe quel iterable avec update() :")
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
print(sep="\n")
print(sep="\n")
print(sep="\n")


print("Supprimer un element avec remove() :")
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
print(sep="\n")
print(sep="\n")
print(sep="\n")


print("Supprimer un element avec discard() :")
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
thisset.discard("bab")

print(thisset)
print("Avec discard(), il n'y a pas d'erreur si l'element n'existe pas.")
print(sep="\n")
print(sep="\n")
print(sep="\n")


print("Exemple d'erreur si l'element n'existe pas :")
thisset = {"apple", "banana", "cherry"}

try:
    thisset.remove("bab")
except KeyError:
    print("Erreur : l'element 'bab' n'existe pas dans l'ensemble.")
