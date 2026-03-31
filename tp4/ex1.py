#Exercice 1: Table de nombres
#Écrivez un programme qui demande à l'utilisateur de saisir la taille d'une table de nombres,
#puis de saisir les éléments de la table. Le programme doit ensuite calculer et afficher la somme, 
#la moyenne, les éléments supérieurs à la moyenne et les éléments inférieurs à la moyenne de la table.

#Voici un exemple de code qui répond à ces exigences :



while True:
    try :
        n = int(input("Entrez le taille de table entier: "))
        print(f"Vous avez entré: {n}")
        break
    except:
        print("Ce n'est pas un nombre entier. Veuillez réessayer.")

t = [n] * n
for i in range(n):
    while True:
        try : 
            t[i] = int(input(f"Entrez l'élément {i} de la table: "))
            break
        except:
            print("Ce n'est pas un nombre entier. Veuillez réessayer.")

print(f"Vous avez entré la table: {t}")

s = 0
for i in range(n):
    s += t[i]
print(f"La somme des éléments de la table est: {s}")

moyenne = s / n
print(f"La moyenne des éléments de la table est: {moyenne}")

tsup = []

for i in range(n):
    if t[i] > moyenne:
        tsup.append(t[i])
print(f"Les éléments de la table qui sont supérieurs à la moyenne sont: {tsup}")

tinf = []
for i in range(n):
    if t[i] < moyenne:
        tinf.append(t[i])   
print(f"Les éléments de la table qui sont inférieurs à la moyenne sont: {tinf}")