class AddPlayerView:

    @staticmethod
    def ask_new_player_information():
        last_name = input("Entrer le nom de famille du nouveau joueur :")
        first_name = input("Entrer le prénom du nouveau joueur :")
        date_of_birth = input("Entrer la date de naissance du nouveau joueur au format JJ/MM/AAAA :")
        chess_code = input("Entrer l'identifiant national d'échecs (deux lettres suivies de cinq chiffres) :")
        print("")
        return [last_name, first_name, date_of_birth, chess_code]

    @staticmethod
    def player_created():
        print(
            "Le joueur a été créé !\n"
            ""
            )