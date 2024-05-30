class ReportPlayersView:

    @staticmethod
    def show_data_players(players):
        for player in players:
            print(
            "\n"
            f"Nom de famille : {player.last_name}\n"
            f"Prénom : {player.first_name}\n"
            f"Date de naissance : {player.date_of_birth}\n"
            ""
            )
        input("Cliquez sur entrer pour continuer.")
        print("")


    @staticmethod
    def empty_data_players():
        print("La liste des joueurs est vide !\n"
              "")
