class MainMenuView:
    @staticmethod
    def input_selection(options):
        print(f"Ajouter un nouveau joueur - { int(options.ADD_PLAYER) } -\n"
              f"Menu tournois - { int(options.TOURNAMENTS) } -\n"
              f"Menu rapports - { int(options.REPORTS) } -\n"
              f"Quitter le programme - { int(options.EXIT) } -")
        return input("Votre choix ? ")