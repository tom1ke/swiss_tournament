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

    def no_data(self):
        print()
        print("Aucune correspondance dans la base de données.")
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
        time_control = self.input_time_control()
        description = input("Description du tournoi : ")

        if name == "":
            print("Vous devez renseigner un nom.")
            return self.input_tournament()
        elif location == "":
            print("Vous devez renseigner un lieu.")
            return self.input_tournament()
        elif start_date == "":
            print("Vous devez renseigner une date de début.")
            return self.input_tournament()
        elif end_date == "":
            print("Vous devez renseigner une date de fin.")
            return self.input_tournament()
        elif description == "":
            print("Vous n'avez pas fourni de description au tournoi.")
            return self.input_tournament()
        else:
            return name, location, start_date, end_date, description, time_control

    def input_time_control(self):
        print("Sélectionnez le format de temps :")
        print("1. Blitz \n"
              "2. Bullet \n"
              "3. Coup rapide")
        print()

        return input("Entrez le numéro de l'option choisie : ")

    def input_player(self):
        print()
        print(f"Ajoutez {NUMBER_OF_PLAYERS} joueurs au tournoi : ")
        print()

        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        date_of_birth = input("Date de naissance (JJ/MM/AAAA) : ")
        gender = input("Sexe (M/F) : ")
        ranking = input("Classement : ")

        try:
            ranking = int(ranking)
        except ValueError:
            print("Le classement du joueur doit être un chiffre.")
            return self.input_player()

        if last_name == "":
            print("Vous devez renseigner un nom de famille.")
            return self.input_player()
        elif first_name == "":
            print("Vous devez renseigner un prénom.")
            return self.input_player()
        elif date_of_birth == "":
            print("Vous devez renseigner une date de naissance.")
            return self.input_player()
        elif gender not in ["M", "F"]:
            print("Veuillez renseigner uniquement \"M\" ou \"F\" pour le sexe.")
            return self.input_player()
        elif ranking < 1:
            print("Le classement du joueur doit être supérieur à 0.")
            return self.input_player()
        else:
            return last_name, first_name, date_of_birth, gender, ranking

    def input_round(self):
        print()
        print("Génération du tour")
        print()

        return input("Nom du tour (ex : \"Round 1\") : ")

    def output_max_round(self):
        print()
        print("Tous les tours du tournoi ont été joués.")
        print()

    def input_results(self, match_):
        print()
        print(f"Entrez le résultat du match {match_} :")
        print()
        player_1_result = input(f"{match_.player_1.first_name} {match_.player_1.last_name} : ")
        player_2_result = input(f"{match_.player_2.first_name} {match_.player_2.last_name} : ")

        return player_1_result, player_2_result

    def output_results_done(self):
        print()
        print("Ce tour à déjà été clôturé.")
        print()

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
