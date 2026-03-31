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