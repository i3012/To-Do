#To-Do List
# 1 : ajouter une tache
# 2 : voir la liste des taches
# 3 : supprimer une tache
# 4 : vider la liste
# 5 : quitter la liste

def Menu():
    print("Menu : ")
    print("1 : ajouter une tache")
    print("2 : voir la liste des taches")
    print("3 : supprimer une tache")
    print("4 : vider la liste")
    print("5 : quitter la liste")

user_input = 'random'
data = list()
while user_input != 5:
    Menu()
    user_input = input("entrer votre choix : ")
    if user_input == '1':
        item = input('entrer la tache que vous voulez faire : ')
        data.append(item)
        print("la tache : " ,item, "  est ajouté a la liste")

    elif user_input == '2':
        print(data)


    elif user_input == '3':
        item_supp = input("entrer la tache que vous avez terminé : ")
        if item_supp in data:
            data.remove(item_supp)
            print("la tache : " +item_supp+ " a ete bien supprime")
        else:
            print("la tache que vous voulez supprimer ne figure pas dans la liste des taches")

    elif user_input == '4':
        yn = input("vous voulez vraiment supprimer la liste des taches : ")
        if yn == True :
            data.clear()
            print(data)
            print("la liste a ete bien supprime")

    elif user_input == '5':
        print("bye bye, a la prochaine")
        break
