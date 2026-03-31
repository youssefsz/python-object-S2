#Exercice 2 : Palindrome
#Écrivez un programme qui demande à l'utilisateur de saisir une chaîne de caractères, puis qui
#identifie et affiche les mots qui sont des palindromes
#(c'est-à-dire des mots qui se lisent de la même manière de gauche à droite et de droite à gauche).
#Le programme doit également afficher les mots inversés.


ch = "binjour radar level python"

print(f"\nla chaine de caractere originale est : {ch} \n")

list = ch.split()

print(f"la liste est : {list} \n")
#print(list[0][::-1])
palindromes = []
inverse = []


for i in range(len(list)):
    inverse.append(list[i][::-1])
    if list[i] == list[i][::-1] :
        palindromes.append(list[i])


print (f"les chaines inversées sont : {inverse} \n")
print(f"les palindromes sont : {palindromes} \n")