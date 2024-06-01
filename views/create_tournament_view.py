class CreateTournamentView:

    @staticmethod
    def warning_message():
        print("ATTENTION, vérifiez bien que tous les participants existent dans la base de données"
              " avant de créer un nouveau tournoi !")

    @staticmethod
    def ask_new_tournament_information():
        name = input("Entrer le nom du tournoi :")
        location = input("Entrer le lieu du tournoi:")
        start_date = input("Entrer la date de début du tournoi :")
        end_date = input("Entrer la date de fin du tournoi :")
        number_of_players = int(input("Entrer le nombre de participants :"))
        description = input("Entrer une description :")
        print("")
        return {"name": name, "location": location, "start_date": start_date, "end_date": end_date,
                "number_of_players": number_of_players, "description": description}

    @staticmethod
    def ask_players_to_add(tournament_information):
        players_to_add = []
        for _ in range(tournament_information["number_of_players"]):
            last_name = input("Entrer le nom de famille du joueur à ajouter au tournoi :")
            first_name = input("Entrer le prénom du joueur à ajouter au tournoi :")
            players_to_add.append([last_name, first_name])
        return players_to_add

    @staticmethod
    def error_message():
        print("Certains joueurs n'ont pas été trouvés, le tournoi n'a pas été créé.\n"
              "Veuillez vérifier dans le rapport des joueurs et créer les joueurs manquants.\n"
              "")

    @staticmethod
    def tournament_created():
        print("Le tournoi a été créé avec succès.")
        input("Cliquez sur entrer pour continuer.")
