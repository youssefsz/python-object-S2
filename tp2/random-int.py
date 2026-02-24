# from random import randint 

# while True : 

#     try : 
#         x = randint(1,9)
#         print(f"the random value is {x} ")

#         while True : 
#             try :
#                 k = int(input("saisir un entier"))
#                 break
    
#             except : 
#                 print("plz put a int !!!")

#         if k == x : 
#             print("nice !!!! u ") 
#         else:
#             print("try again :-(")
            
#             while True :
                
#                 h = input("if u want to try again press 'y' or leave using 'q' :  ")
#                 if h == 'y' or h == 'q':

#                     break
#                 else :
#                     print("saisir y ou q !!!!")
            
                    

#             if h == 'q' :
#                 break

        


#     except :
#         print("somthing went wrong hahahahahah !!")


#------------------Youssef work :)-------------------------

#JEU DU NOMBRE MYSTÈRE  

from random import *

n = randint(0, 100)
print(n)
essais = 0
score = 0
u = -1

while u != n and essais < 5:
    saisie = input("A quel nombre vous pensez ? (0-100) : ")
    
    while not saisie.isdigit() or not (0 <= int(saisie) <= 100):
        print("⚠ Erreur : veuillez saisir un nombre entier entre 0 et 100.")
        saisie = input("A quel nombre vous pensez ? (0-100) : ")
        
    u = int(saisie)
    essais += 1
    score += 1
    
    if u > n:
        print("Le nombre cherché est plus petit.")
    elif u < n:
        print("Le nombre cherché est plus grand.")

# --- Résultat final ---
if u == n:
    print("\n Bravo ! Vous avez trouvé le nombre.")
    print("Score =", score)
else:
    print("\n ❌ Trop tard ! Vous avez utilisé tous vos essais.")
    print("Le nombre était :", n)





