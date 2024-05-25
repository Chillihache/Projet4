class View:

    @staticmethod
    def ask_new_player_information():
        last_name = input("Veuillez entrer le nom de famille du nouveau joueur :")
        first_name = input("Veuillez entrer le prénom du nouveau joueur :")
        date_of_birth = input("Veuillez entrer la date de naissance du nouveau joueur au format JJ/MM/AAAA :")
        return [last_name, first_name, date_of_birth]

    @staticmethod
    def player_created():
        print("le joueur a été créé !")

    @staticmethod
    def show_data_players(data_players):
        for players in range(len(data_players)):
            print(data_players[players])

    @staticmethod
    def empty_data_players():
        print("La liste des joueurs est vide !")


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
        return {"name": name, "location": location, "start_date": start_date, "end_date": end_date,
                "number_of_players": number_of_players, "description": description}

    @staticmethod
    def find_a_player():
        last_name = input("Entrer le nom de famille du joueur à ajouter au tournoi :")
        first_name = input("Entrer le prénom du joueur à ajouter au tournoi :")
        return [last_name, first_name]

    @staticmethod
    def player_found(player_found):
        print(f"{player_found["First name"]} {player_found["Last name"]} a été ajouté au tournoi !")

    @staticmethod
    def player_not_found(player_to_find):
        print(f"{player_to_find[1]} {player_to_find[0]} n'a pas été trouvé dans la base de données.")
        print("Le tournoi n'a pas pu être créé.")

    @staticmethod
    def tournament_created():
        print("Le tournoi a été créé avec succès !")

    @staticmethod
    def show_tournaments_names_and_start_date(data_tournaments):
        for tournaments in data_tournaments:
            print(tournaments["Name"], tournaments["Start date"])

    @staticmethod
    def ask_tournament_to_find():
        tournament_name = input("Entrer le nom du tournoi :")
        return tournament_name



    @staticmethod
    def show_tournament_information(tournament_information):
        for element in tournament_information:
            print(f"{element} : {tournament_information[element]}")

    @staticmethod
    def tournament_not_found():
        print("Aucun tournoi n'a été trouvé.")







