# Exercice 1
# Créer un dictionnaire D qui associe à chaque nom d'une personne son âge. un Dictionnair Majeur et DMineur qui associe à chaque nom d'une personne majeur ou mineur.

D = {'albert': 29, 'bob': 16, 'charlie': 18 , 'dave': 21, 'eve': 17}
Majeur = {}
Mineur = {}
#for x, z in D.items():
#    print(x)
#    print(z)


for nom, age in D.items():
    if age >= 18:
        Majeur[nom] = age
    else:
        Mineur[nom] = age

print("Dictionnaire des majeurs:", Majeur)
print("Dictionnaire des mineurs:", Mineur)
