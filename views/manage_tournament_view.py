class ManageTournamentView:

    @staticmethod
    def tournament_not_found():
        print("Aucun tournoi correspondant n'a été trouvé, veuillez vérifier dans la liste des tournois.")
        input("Cliquez sur entrer pour continuer.")
        print("")

    @staticmethod
    def generate_round(current_round):
        input(f"Cliquez sur entrer pour générer le round {current_round}")
        print("")

    @staticmethod
    def round_generated(tournament):
        print(f"Le tour {tournament.current_round} a été généré. \n"
              "Voici les matchs pour ce tour :")
        for match in tournament.rounds[tournament.current_round - 1].matchs:
            print(match)
        input("Cliquez sur entrer pour continuer.")
        print("")

    @staticmethod
    def ask_winner(match):
        print(f"Sélectionnez le vainqueur du match {match} \n"
              f"{match[0][0]}      - 1 - \n"
              f"{match[1][0]}      - 2 - \n"
              f"Egalité            - 3 - \n"
              "")
        choice = int(input("Votre choix : "))
        return choice

    @staticmethod
    def show_winners(tournament):
        print(f"Voici les scores du tour {tournament.current_round}")
        for match in tournament.rounds[tournament.current_round-1].matchs:
            print(match)
        input("Cliquez sur entrer pour continuer")
        print("")

    @staticmethod
    def tournament_closed():
        print("Le tournoi est terminé ! \n"
              "")
        input("Cliquez sur entrer pour continuer.")



