import argparse


def analyser_commande():
    """
    Reçoit et traite une commande envoyé par un utilisateur via un terminal ou une console.
    :return: l'objet d'arguments généré avec le module argparse.
    """
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument('IDUL', metavar='IDUL',
                        default='JUGUA17', help="IDUL du joueur")
    parser.add_argument('-l', '--lister', dest='liste',
                        help='Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()


def afficher_damier_ascii(etat_de_jeu):
    """
    Affiche à la console une partie, soit le positionnement des pions et des murs sur un damier.
    :param etat_de_jeu: Un dictionnaire json contenant les clés 'joueurs' et 'murs'.
    :return: Ne retourne rien, mais affiche un damier à la console.
    """
    pion, vertical, horizontal = [], [], []
    for i in range(9):
        matrice_pion, matrice_verticale, matrice_horizontale = [], [], []
        for j in range(9):
            matrice_pion.append('.')
            matrice_verticale.append(' ')
            matrice_horizontale.append('   ')
        pion.append(matrice_pion)
        vertical.append(matrice_verticale)
        horizontal.append(matrice_horizontale)
    posi_j_1 = etat_de_jeu['joueurs'][0]['pos']
    posi_j_2 = etat_de_jeu['joueurs'][1]['pos']
    pion[posi_j_1[1] - 1][posi_j_1[0] - 1] = '1'
    pion[posi_j_2[1] - 1][posi_j_2[0] - 1] = '2'
    pion.reverse()
    for a, b in etat_de_jeu['murs']['horizontaux']:
        horizontal[b - 1][a - 1] = '---'
    horizontal.reverse()
    for a, b in etat_de_jeu['murs']['verticaux']:
        vertical[b - 1][a - 1] = '|'
    vertical.reverse()
    damier_ascii = "   -----------------------------------\n"
    for i in range(9):
        if i == 8:
            damier_ascii += "1 |"
            for j in range(9):
                if j == 0:
                    damier_ascii += "{}{} ".format(vertical[8][j], pion[8][j])
                else:
                    damier_ascii += "{} {} ".format(vertical[8][j], pion[8][j])
            damier_ascii += "|\n"
        else:
            damier_ascii += "{} |".format(9 - i)
            for j in range(9):
                if j == 0:
                    damier_ascii += "{}{} ".format(
                        vertical[i][j] if vertical[i + 1][j] != '|' else '|', pion[i][j]
                    )
                else:
                    damier_ascii += "{} {} ".format(
                        vertical[i][j] if vertical[i + 1][j] != '|' else '|', pion[i][j]
                    )
            damier_ascii += "|\n"
            damier_ascii += "  |"
            for j in range(9):
                if j == 0:
                    damier_ascii += "{}{}".format(
                        horizontal[i][j],
                        '-' if horizontal[i][j] == '---' else vertical[i + 1 if i < 8 else 0][j + 1]
                    )
                else:
                    damier_ascii += "{}{}".format(
                        horizontal[i][j] if horizontal[i][j - 1] != '---' else '---',
                        '-' if horizontal[i][j] == '---' else vertical[i + 1 if i < 8 else 0][j + 1 if j < 8 else 0]
                    )
            damier_ascii = damier_ascii[:-1]
            damier_ascii += "|\n"
    damier_ascii += "--|-----------------------------------\n"
    damier_ascii += "  | 1   2   3   4   5   6   7   8   9\n"
    print(damier_ascii)
