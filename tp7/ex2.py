
print("--- Saisie des informations pour 5 joueurs ---")
joueurs = []
for i in range(2):
    print(f"\n--- Joueur {i+1} ---")
    joueur = {}
    joueur['num_joueur'] = input("Entrez le numéro du joueur : ")
    joueur['nom_joueur'] = input("Entrez le nom du joueur : ")
    joueur['prenom_joueur'] = input("Entrez le prénom du joueur : ")
    joueur['prix_joueur'] = input("Entrez le prix du joueur : ")
    joueur['nom_equipe'] = input("Entrez le nom de l'équipe du joueur : ")
    joueurs.append(joueur)

print("\n--- Liste des joueurs saisis ---")
print(joueurs)  

equipes = {}
for joueur in joueurs:
    nom_equipe = joueur['nom_equipe']
    if nom_equipe not in equipes:
        equipes[nom_equipe] = []
    equipes[nom_equipe].append(joueur['nom_joueur'])

print("\n--- Regroupement par équipe ---")
print(equipes)