from itertools import chain
from views.views import View
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match
from util import TABLE_TOURNAMENTS, TABLE_PLAYERS, NUMBER_OF_ROUNDS, NUMBER_OF_PLAYERS, CREATE_TOURNAMENT, \
    GENERATE_ROUND, ENTER_RESULTS, LOAD_PREVIOUS_STATE, REPORTS, QUIT, ALL_ACTORS, TOURNAMENTS, PLAYERS, ROUNDS, \
    MATCHES, MAIN_MENU, COMPLETED, SORT_ALPHA, SORT_RANK


class Controller:
    """
    Classe représentant un contrôleur
    """

    def __init__(self):
        """
        Constructeur de la classe Controller
        self.view : Instancie une vue
        """
        self.view = View()

    def run(self):
        """
        Métode d'exécution du programme
        Appelle View.welcome et View.end_program pour les messages d'accueil et de sortie
        Appelle Controller.run_main pour le menu principal
        """
        self.view.welcome()

        self.run_main_menu()

        self.view.end_program()

    def run_main_menu(self):
        """
        Boucle de menu principal
        En fonction du choix utilisateur via View.input_main
        """
        operation = self.view.input_main()

        while operation != QUIT:
            """
            La boucle s'arrête si l'utilisateur choisi de quitter le programme
            """

            if operation == CREATE_TOURNAMENT:
                """
                Instancie un tournoi et ses joueurs et l'enregistre en base de données
                """
                current_tournament = self.create_tournament()

                player_index = 0
                while len(current_tournament.player_list) < NUMBER_OF_PLAYERS:
                    player_index += 1
                    current_player = self.add_player()
                    current_player.index = player_index
                    current_tournament.player_list.append(current_player)
                    TABLE_PLAYERS.insert(current_player.serialize_player())

                TABLE_TOURNAMENTS.insert(current_tournament.serialize_tournament())

                self.view.output_generic(current_tournament)

            elif operation == GENERATE_ROUND:
                """
                Instancie le dernier tournoi disponible en base de données et génère le prochain tour si le nombre de
                tour maximum n'est pas atteint
                Met à jour le tournoi en base de données
                """
                try:
                    last_tournament = TABLE_TOURNAMENTS.all()[-1]
                    current_tournament = self.load_tournament(last_tournament)
                    if len(current_tournament.round_list) >= NUMBER_OF_ROUNDS:
                        self.view.output_max_round()
                    else:
                        current_round = Round(self.view.input_round())
                        current_tournament.round_list.append(current_round)
                        current_round.match_list = self.match_players(current_tournament)
                        current_tournament.player_list = self.sort_players_by_rank(current_tournament.player_list)

                        TABLE_TOURNAMENTS.update(current_tournament.serialize_tournament(),
                                                 doc_ids=[last_tournament.doc_id])

                        self.view.output_generic(current_tournament)

                except IndexError:
                    """
                    Si aucun tournoi n'est enregistré dans la base de données
                    """
                    raise IndexError
                    # self.view.no_data()

            elif operation == ENTER_RESULTS:
                """
                Instancie le dernier tournoi disponible en base de données et permet de mettre à jour les résultats
                des matchs du dernier tour disponible si celui-ci n'est pas clôturé
                Met à jour le tournoi en base de données
                """
                try:
                    last_tournament = TABLE_TOURNAMENTS.all()[-1]
                    current_tournament = self.load_tournament(last_tournament)
                    current_round = current_tournament.round_list[-1]
                    if current_round.completed:
                        self.view.output_results_done()
                    else:
                        self.update_scores(current_round, current_tournament)
                        self.complete_round(current_round)
                        current_tournament.player_list = self.sort_players_by_rank(current_tournament.player_list)

                        TABLE_TOURNAMENTS.update(current_tournament.serialize_tournament(),
                                                 doc_ids=[last_tournament.doc_id])

                        self.view.output_generic(current_tournament)

                except IndexError:
                    """
                    Si aucun tournoi n'est enregistré dans la base de données
                    """
                    self.view.no_data()

            elif operation == LOAD_PREVIOUS_STATE:
                """
                Instancie le dernier tournoi disponible en base de données pour l'afficher
                """
                try:
                    last_tournament = TABLE_TOURNAMENTS.all()[-1]
                    current_tournament = self.load_tournament(last_tournament)
                    current_tournament.player_list = self.sort_players_by_rank(current_tournament.player_list)
                    self.view.output_generic(current_tournament)

                except IndexError:
                    """
                    Si aucun tournoi n'est enregistré dans la base de données
                    """
                    self.view.no_data()

            elif operation == REPORTS:
                """
                Appelle Controller.run_reports_menu pour accéder au menu des rapports
                """
                self.run_reports_menu()

            else:
                """
                Si le choix de l'utilisateur ne fait pas partie des choix disponibles
                """
                self.view.invalid_choice()

            operation = self.view.input_main()

    def run_reports_menu(self):
        """
        Boucle de menu des rapports
        En fonction du choix utilisateur via View.input_reports
        """
        report_op = self.view.input_reports()

        while report_op != MAIN_MENU:
            """
            La boucle s'arrête si l'utilisateur choisi de retourner au menu principal
            """

            if report_op == ALL_ACTORS:
                """
                Affiche la liste de tous les acteurs enregistrés danns la table des joueurs, par ordre alphabétique ou
                par classement sauf si aucune donnée n'est disponible en base de données
                """
                player_list = self.display_mode(self.load_players_from_db())
                self.indexing_output(player_list)

                if len(player_list) == 0:
                    self.view.no_data()

            elif report_op == TOURNAMENTS:
                """
                Affiche la liste de tous les tournois enregistrés dans la table des tournois sauf si aucune donnée
                n'est disponible en base de données
                """
                tournament_list = self.load_tournaments_from_db()
                self.indexing_output(tournament_list)

                if len(tournament_list) == 0:
                    self.view.no_data()

            elif report_op == PLAYERS:
                """
                L'utilisateur choisi un tournoi avec son index (disponible dans la liste des tournois) et affiche la
                liste de ses joueurs, sauf si aucune donnée n'est disponible au sein du tournoi
                """
                try:
                    selected_tournament = self.select_tournament_from_db()
                    self.indexing_output(selected_tournament.player_list)

                except AttributeError:
                    self.view.no_data()

            elif report_op == ROUNDS:
                """
                L'utiliateur choisi un tournoi avec son index (disponible dans la liste des tournois) et affiche la
                liste de ses tours, sauf si aucune donnée n'est disponible au sein du tournoi
                """
                try:
                    selected_tournament = self.select_tournament_from_db()
                    self.indexing_output(selected_tournament.round_list)

                except AttributeError:
                    self.view.no_data()

            elif report_op == MATCHES:
                """
                L'utiliateur choisi un tournoi avec son index (disponible dans la liste des tournois) et affiche la
                liste de ses matchs, sauf si aucune donnée n'est disponible au sein du tournoi
                """
                try:
                    selected_tournament = self.select_tournament_from_db()
                    all_match_lists = [round_.match_list for round_ in selected_tournament.round_list]
                    self.indexing_output(chain(*all_match_lists))

                except AttributeError:
                    self.view.no_data()

            else:
                """
                Si le choix de l'utilisateur ne fait pas partie des choix disponibles
                """
                self.view.invalid_choice()

            report_op = self.view.input_reports()

    def create_tournament(self):
        """
        Instancie un tournoi à partir des entrées utilisateur dans View.input_player
        :return: Instance de tournoi
        """
        return Tournament(*self.view.input_tournament())

    def add_player(self):
        """
        Instancie un joueur à partir des entrées utilisateur dans View.input_player
        :return: Instance de joueur
        """
        return Player(*self.view.input_player())

    def load_tournament(self, db_tournament):
        """
        Instancie un tournoi sérialisé de la base de données. Instancie également les joueurs, tours et matchs stockés
        dans le tournoi
        :param db_tournament: Tournoi sérialisé
        :return: Instance de tournoi
        """
        loaded_tournament = Tournament(**db_tournament)

        loaded_players = [Player(**player) for player in loaded_tournament.player_list]
        loaded_tournament.player_list.clear()
        for player in loaded_players:
            loaded_tournament.player_list.append(player)

        loaded_rounds = [Round(**round_) for round_ in loaded_tournament.round_list]
        loaded_tournament.round_list.clear()
        for round_ in loaded_rounds:
            loaded_tournament.round_list.append(round_)

            loaded_matches = [Match(**match_) for match_ in round_.match_list]
            round_.match_list.clear()
            for match_ in loaded_matches:
                match_.player_1 = Player(**match_.player_1)
                match_.player_2 = Player(**match_.player_2)
                round_.match_list.append(match_)

        return loaded_tournament

    def load_tournaments_from_db(self):
        """
        Charge tous les tournois sérialisés dans la table des tournois, les instancie, et les ajoute à une liste vide
        :return: Liste d'instances de tournois
        """
        tournament_list = []
        for tournament in TABLE_TOURNAMENTS.all():
            loaded_tournament = self.load_tournament(tournament)
            tournament_list.append(loaded_tournament)
        return tournament_list

    def select_tournament_from_db(self):
        """
        Instancie un tournoi sérialisé de la base données sélectionné par l'utilisateur avec
        View.input_reports_tournament_choice
        Si l'index de tournoi existe dans la base données :
        :return: Instance de tournoi
        Sinon:
        :return: Message d'erreur avec View.invalid_choice
        """
        tournament_list = self.load_tournaments_from_db()
        tournament_index = (int(self.view.input_reports_tournament_choice()) - 1)
        if 0 <= tournament_index < len(tournament_list):
            return self.load_tournament(TABLE_TOURNAMENTS.all()[tournament_index])
        else:
            return self.view.invalid_choice()

    def load_players_from_db(self):
        """
        Charge tous les joueurs sérialisés dans la table des joueurs, les instancie, et les ajoute à une liste vide
        :return: Liste d'instances de joueurs
        """
        player_list = []
        for player in TABLE_PLAYERS.all():
            loaded_player = Player(**player)
            player_list.append(loaded_player)
        return player_list

    def sort_players_by_rank(self, player_list):
        """
        Classe des instances de joueurs par score puis par classement en ordre décroissant
        :param player_list: Liste d'instances de joueurs
        :return: Liste classée d'instances de joueurs
        """
        return sorted(player_list, key=lambda player: (player.score, player.ranking), reverse=True)

    def sort_players_by_name(self, player_list):
        """
        Classe des instances de joueurs par ordre alphabétique grâce au nom et prénom
        :param player_list: Liste d'instances de joueurs
        :return: Liste classée d'instances de joueurs
        """
        return sorted(player_list, key=lambda player: (player.last_name, player.first_name))

    def match_players(self, tournament):
        """
        Génère la liste et instancie les matchs du prochain tour d'un tournoi
        :param tournament: Instance de tournoi
        :return: Liste d'instances de matchs
        """
        round_match_list = []
        sorted_players = self.sort_players_by_rank(tournament.player_list)

        if len(tournament.round_list) == 1:
            """
            Si le tour concerné est le premier du tournoi
            """
            half_number_of_players = len(sorted_players) // 2

            for i in range(half_number_of_players):
                player_1 = sorted_players[i]
                player_2 = sorted_players[i+half_number_of_players]
                pair = Match(player_1, player_2)
                round_match_list.append(pair)

        elif len(tournament.round_list) > 1:
            """
            Pour les autres tours
            """
            played_matches = self.check_played_matches()
            used_players = []
            unmatchable_players = []

            while len(round_match_list) != 4:
                unmatchable_players.clear()
                player_1 = self.get_matchable_player(sorted_players, used_players, unmatchable_players)
                unmatchable_players.append(player_1)
                player_2 = self.get_matchable_player(sorted_players, used_players, unmatchable_players)

                for match_ in played_matches:
                    if match_.player_1.index in [
                        player_1.index,
                        player_2.index,
                    ] and match_.player_2.index in [player_1.index, player_2.index]:
                        unmatchable_players.append(player_2)
                        player_2 = self.get_matchable_player(sorted_players,
                                                             used_players,
                                                             unmatchable_players)

                        if player_2 is None:
                            match_to_break = round_match_list[-1]
                            used_players = list(filter(lambda x: x not in [match_to_break.player_1,
                                                                           match_to_break.player_2],
                                                       used_players))
                            round_match_list.remove(match_to_break)
                            player_2 = self.get_matchable_player(sorted_players,
                                                                 used_players,
                                                                 unmatchable_players)

                used_players.extend([player_1, player_2])
                pair = Match(player_1, player_2)
                round_match_list.append(pair)

        return round_match_list

    def get_matchable_player(self, sorted_players, used_players, unmatchable_players):
        default_value = None
        return next(
            (
                player
                for player in sorted_players
                if player not in used_players and player not in unmatchable_players
            ),
            default_value,
        )

    def check_played_matches(self):
        """
        Instancie le dernier tournoi enregistré en base de données et constitue une liste de matchs déjà joués à partir
        des listes de matchs de chaque tour existant du tournoi
        :return: Liste d'instances de matchs
        """
        last_tournament = TABLE_TOURNAMENTS.all()[-1]
        current_tournament = self.load_tournament(last_tournament)
        all_match_lists = [round_.match_list for round_ in current_tournament.round_list]
        return list(chain(*all_match_lists))

    def update_scores(self, round_, tournament):
        """
        Met à jour les scores des joueurs sur les matchs d'un tour en fonction des entrées utilisateur via
        View.input_results
        :param round_: Instance de tour
        :param tournament: Instance de tournoi
        """
        for match_ in round_.match_list:
            results = (self.view.input_results(match_))
            match_.player_1_result = float(results[0])
            match_.player_2_result = float(results[1])

            for player in tournament.player_list:
                if player.index == match_.player_1.index:
                    player.score = player.score + match_.player_1_result
                elif player.index == match_.player_2.index:
                    player.score = player.score + match_.player_2_result

    def complete_round(self, round_):
        """
        Détermine le statut du tour
        :param round_: Instance de tour
        Si l'utilisateur choisi de clôturer le tour avec View.input_completed_round :
        :return: Le paramètre "completed" du tour passe à True
        Sinon :
        :return: Le paramètre "completed" du tour reste False
        """
        round_state = self.view.input_completed_round()
        if round_state == COMPLETED:
            round_.completed = True

    def display_mode(self, list_to_sort):
        """
        Trie les éléments d'une liste d'instances de joueurs en ordre alphabétique ou par classement en fonction du
        choix utilisateur
        :param list_to_sort: Liste d'instances de joueurs
        :return: Liste classée d'instances de joueurs
        """
        display_mode = self.view.input_display_mode()
        if display_mode == SORT_ALPHA:
            list_to_sort = self.sort_players_by_name(list_to_sort)
        elif display_mode == SORT_RANK:
            list_to_sort = self.sort_players_by_rank(list_to_sort)
        else:
            self.view.invalid_choice()
        return list_to_sort

    def indexing_output(self, obj_list):
        """
        Formate une liste pour l'affichage, avec, ligne par ligne, l'index et la valeur de l'élément
        Appelle la méthode View.output_indexed pour l'affichage
        :param obj_list: Liste d'objets
        :return: Liste formatée d'objets
        """
        return [self.view.output_indexed(index, obj) for index, obj in enumerate(obj_list, start=1)]
