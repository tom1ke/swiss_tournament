from util import NUMBER_OF_PLAYERS


class View:

    def welcome(self):
        print()
        print("Centre Échecs : Bienvenue sur le gestionnaire de tournoi")
        print()

    def end_program(self):
        print("À bientôt !")

    def input_main(self):
        print()
        print("Menu principal : ")
        print()
        print("1. Créer un tournoi \n"
              "2. Générer le prochain tour \n"
              "3. Entrer les résultats du tour \n"
              "4. Charger la dernière sauvegarde \n"
              "5. Sauvegarder & quitter")
        print()

        return input("Entrez le numéro de l'option choisie : ")

    def input_tournament(self):
        print()
        print("Création d'un nouveau tournoi : ")
        print()

        name = input("Nom du tournoi : ")
        location = input("Lieu du tournoi : ")
        start_date = input("Date de début (JJ/MM/AA) : ")
        end_date = input("Date de fin (JJ/MM/AAAA) : ")
        time_control = input("Bullet, Blitz ou Coup rapide : ")
        description = input("Description du tournoi : ")

        return name, location, start_date, end_date, time_control, description

    def input_player(self):
        print()
        print(f"Ajoutez {NUMBER_OF_PLAYERS} joueurs au tournoi : ")
        print()

        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        date_of_birth = input("Date de naissance (JJ/MM/AAAA) : ")
        gender = input("Sexe (M/F) : ")
        ranking = input("Classement : ")

        return last_name, first_name, date_of_birth, gender, ranking

    def input_round(self):
        print()
        print("Génération du tour")
        print()

        return input("Nom du tour (ex : \"Round 1\") : ")

    def enter_results(self):
        index = 1
        while index <= NUMBER_OF_PLAYERS:
            print()
            input(f"Entrez le résultat (1 : victoire, 0.5 : nul, 0 : défaite) pour le joueur {index} :")
            index += 1
