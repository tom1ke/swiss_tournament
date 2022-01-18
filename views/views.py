from util import NUMBER_OF_PLAYERS


class View:

    def end_program(self):
        print("À bientôt !")

    def input_main(self):
        print()
        print("Centre Échecs : Bienvenue sur le gestionnaire de tournoi")
        print()
        print("Menu : ")
        print()
        print("1. Créer un tournoi \n"
              "2. Charger dernière sauvegarde \n"
              "3. Générer le prochain tour \n"
              "4. Quitter")
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
