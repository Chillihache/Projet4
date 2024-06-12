class ReportTournamentsView:

    @staticmethod
    def show_tournaments_list(tournaments):
        print("Voici la liste des tournois :")
        for tournament in tournaments:
            print(tournament.name)
        print("")
        input("Cliquez sur entrer pour continuer ")
        print("")

    @staticmethod
    def ask_tournament_name():
        tournament_name = input("Entrer le nom du tournoi :")
        return tournament_name

    @staticmethod
    def show_tournament_name_dates(tournament):
        if tournament:
            print(f"Nom du tournoi : {tournament.name} \n"
                  f"Date de début : {tournament.start_date} \n"
                  f"Date de fin : {tournament.end_date} \n"
                  "")
            input("Cliquez sur entrer pour continuer.")
        else:
            print("Aucun tournoi n'a été trouvé.")
            input("Cliquez sur entrer pour continuer")

    @staticmethod
    def show_tournament_rounds_matchs(tournament):
        print("")
        for i in range(len(tournament.rounds)):
            print(f"{tournament.rounds[i].name} \n"
                  f"Date de début : {tournament.rounds[i].start_date} \n"
                  f"Date de fin : {tournament.rounds[i].end_date}"
                  )
            for match in tournament.rounds[i].matchs:
                print(match)
            print("")
