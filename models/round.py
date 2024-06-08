from random import shuffle
from helpers.json_helper import JsonHelper


class Round:

    def __init__(self, players):
        self.players = players
        self.matchs = []
        self.json_helper = JsonHelper("data\data_tournaments.json")
        self.players_and_scores = []

    # TODO: Tournament or member variable of tournament should probably be in init
    def generate(self, tournament, current):
        if current == 1:
            for player in self.players:
                self.players_and_scores.append([player.first_name + " " + player.last_name, 0])
            shuffle(self.players_and_scores)
            for i in range(int(len(self.players_and_scores)/2)):
                self.matchs.append((self.players_and_scores[i],
                                    self.players_and_scores[len(self.players_and_scores) - i - 1]))

        else:
            # On veut savoir quel joueur a joué contre quels joueurs et quel est le score des joueurs ?
            # Reprendre les matchs précédents -> Faire une liste de tuple avec en premier element le joueur, en deuxième element,
            # la liste des joueurs qu'il a déjà affronté -> Ca va donner un genre de matrice.

            # On veut deux listes : Une liste des joueurs matchés et une liste des joueurs restants -> La somme de la longueur de ces
            # deux listes doit toujours être égale à la longueur de la liste des joueurs du tournoi.
            # Trier la liste des joueurs restants par score -> Si on avait pas voulu trier avec les joueurs déjà affrontés
            # On aurait fait matchs = [[sorted_players[i * 2], sorted_players[i * 2 + 1]] for i in range(len(sorted_players) / 2)]

            # Jusqu'à ce que la liste des joueurs restant soit vide -> Attention, toujours bien retirer deux joueurs de cette liste par match
            #   Jusqu'à ce qu'on atteigne la fin de la liste des joueurs restants - le premier joueur restant
            #     Si le joueur a déjà été affronté -> joueur suivant
            #     Si c'est le dernier joueurs de la liste des joueurs restants OU si le joueur n'a pas déjà été affronté -> on le match -> on retire les deux joueurs de la liste des joueurs restants -> on les ajoute à la liste des joueurs matchés
            #       Break ou return si c'est checké dans une fonction
            # Rappel : On peut utiliser pop pour sortir un element d'une liste

            # TODO: Respecter le pseudo-code
            # hint: On préfére utiliser des joueurs que des structures moins précises -> Peut être rajouter les fonctions necessaires dans joueurs (pour les comparer, transformer, ...)
            # Potentiellement, recommencer à zero les parties qui ne fonctionnent pas pour bien s'imprimer la logique et trouver les points manquants

            for match in tournament.rounds[current - 2].matchs:
                self.players_and_scores.append(match[0])
                self.players_and_scores.append(match[1])

            self.players_and_scores = sorted(self.players_and_scores, key=lambda x: x[1], reverse=True)

            previous_matchs = []
            for i in range(current - 1):
                for match in (tournament.rounds[i].matchs):
                    previous_matchs.append([match[0][0], match[1][0]])
                    previous_matchs.append([match[1][0], match[0][0]])

            while len(self.players_and_scores) != 0:
                self.find_a_match(previous_matchs)

    def find_a_match(self, previous_matchs):

        for j in range(len(self.players_and_scores)):
            if [self.players_and_scores[0][0], self.players_and_scores[j][0]] not in previous_matchs:
                self.matchs.append((self.players_and_scores[0], self.players_and_scores[j]))
                del self.players_and_scores[0]
                del self.players_and_scores[j]
                break


































