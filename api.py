import requests
import json


def lister_parties(idul):
    url_lister = 'https://python.gel.ulaval.ca/quoridor/api/lister/'
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

        
def initialiser_partie(idul):
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
        
