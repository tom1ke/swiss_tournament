from util import NUMBER_OF_PLAYERS


class View:

    def welcome(self):
        print()
        print("Centre Échecs : Bienvenue sur le gestionnaire de tournoi")
        print()

    def end_program(self):
        print("À bientôt !")

    def invalid_choice(self):
        print()
        print("Votre choix n'est pas valide, vous devez renseigner une option existante.")
        print()

    def input_main(self):
        print()
        print("Menu principal : ")
        print()
        print("1. Créer un tournoi \n"
              "2. Générer le prochain tour \n"
              "3. Entrer les résultats du tour \n"
              "4. Charger la dernière sauvegarde \n"
              "5. Rapports \n"
              "6. Sauvegarder & quitter")
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

    def input_results(self, match_):
        index = 1
        while index <= NUMBER_OF_PLAYERS:
            print()
            input(f"Entrez le résultat (1 : victoire, 0.5 : nul, 0 : défaite) pour le joueur {index} : ")
            index += 1

    def input_completed_round(self):
        print()
        print("Le tour est-il terminé :")
        print()
        print("1. Oui \n"
              "2. Non")
        print()

        return input("Entrez le numéro de l'option choisie : ")

    def input_reports(self):
        print()
        print("Rapports :")
        print()
        print("1. Tous les joueurs enregistrés \n"
              "2. Tous les tournois enregistrés \n"
              "3. Tous les joueurs du tournoi sélectionné \n"
              "4. Tous les tours du tournoi sélectionné \n"
              "5. Tous les matchs du tournoi sélectionné \n"
              "6. Menu principal")
        print()
        return input("Entrez le numéro de l'option choisie : ")

    def input_reports_tournament_choice(self):
        print()
        return input("Entrez le numéro du tournoi concerné (cf. Tournois enregistrés) : ")

    def input_display_mode(self):
        print()
        print("Mode d'affichage :")
        print()
        print("1. Par ordre alphabétique \n"
              "2. Par classement")
        print()
        return input("Entrez le numéro de l'option choisie : ")

    def output_generic(self, obj):
        return print(obj)

    def output_indexed(self, index, obj):
        return print(index, obj)
