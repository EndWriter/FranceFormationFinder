# ce fichier est pour la récupération du contenu HTML
import requests

# fonction pour récupérer le HTML d'une page web
def fetch_html(url, headers=None, timeout=10):
	# je récupère le HTML d'une page web
	response = requests.get(url, headers=headers, timeout=timeout)
	# je vérifie que la requête a réussi
	response.raise_for_status()
	# je retourne le contenu HTML
	return response.text
