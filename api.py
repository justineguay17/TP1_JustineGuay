import json
import requests


def lister_parties(idul):
    """
    Permet d'obtenir la liste des dernières parties démarrées ou terminées par le joueur de l'idul.
    Les parties sont listées à partir du serveur du cour.
    :param idul: Chaine de caractère associée au dossier du joueur.
    :return: Ne retourne rien. Affiche à la console un dictionnaire json.
    """
    url_lister = 'https://python.gel.ulaval.ca/quoridor/api/lister/'
    try:
        response = requests.get(url_lister, params={'idul': idul})
        if response.status_code == 200:
            response = response.text
            json_var = json.loads(response)
            json_str = json.dumps(json_var, indent=2)
            print(json_str)
        else:
            print("Le GET sur '{}' a produit le code d'erreur {}.".format(
                url_lister, response.status_code)
            )
    except RuntimeError as error:
        print(error)


def initialiser_partie(idul):
    """
    Permet de démarrer une partie contre le robot du serveur du cour.
    :param idul: Chaine de caractère associée au dossier du joueur.
    :return: Retourne le tuple ( identification de partie , état de jeu )
    """
    url_init = 'https://python.gel.ulaval.ca/quoridor/api/initialiser/'
    try:
        response = requests.post(url_init, data={'idul': idul})
        if response.status_code == 200:
            json_res = response.json()
            return json_res['id'], json_res['état']
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}.".format(
                url_init, response.status_code)
            )
    except RuntimeError as error:
        print(error)


def jouer_coup(id_partie, type_coup, position):
    """
    Permet de jouer un coup contre le robot du serveur du cour.
    :param id_partie: La chaine de caractère identifiant la partie.
    :param type_coup: 'D' pour déplacement, 'MH' pour mur horizontal et pout 'MV' mur vertical.
    :param position: Un tuple ( x, y ) pour positionner un déplacement ou un mur.
    :return: Si sans erreur, un dictionnaire json d'état de jeu.
    """
    url_coup = 'https://python.gel.ulaval.ca/quoridor/api/jouer/'
    try:
        response = requests.post(url_coup, data={
            'id': id_partie, 'type': type_coup, 'pos': position}
        )
        if response.status_code == 200:
            json_res = response.json()
            if 'gagnant' in json_res:
                raise StopIteration(json_res['gagnant'])
            elif 'message' in json_res:
                print(json_res['message'])
            else:
                return json_res
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}.".format(
                url_coup, response.status_code)
            )
    except RuntimeError as error:
        print(error)

