
from bs4 import BeautifulSoup
# on utilise BeautifulSoup pour parser le HTML

def parse_formations(html):
	
	soup = BeautifulSoup(html, "html.parser")
	# on initialise formation comme un tableau vide
	formations = []
	# pour chaque formation qui compose le html
    # on vient cibler les éléments que l'on souhaite extraire
	for li in soup.select("ul.result-list > li.result"):
		# titre et lien de formation
		a_title = li.select_one("h2.t4.media-heading a")
		title = a_title.get_text(strip=True) if a_title else ""
		link = a_title["href"] if a_title and a_title.has_attr("href") else ""
		# description
		desc = li.select_one("p.description")
		description = desc.get_text(strip=True) if desc else ""
		# le type de formation
		type_ = li.select_one("p.type")
		type_formation = type_.get_text(strip=True) if type_ else ""
		# le taux de retour à l'emploi
		rate = li.select_one("span.rate-value")
		taux_retour = rate.get_text(strip=True) if rate else ""

        # on vient ajouter sous forme d'objet nos formations
		formations.append({
			"title": title,
			"link": link,
			"description": description,
			"type": type_formation,
			"taux_retour_emploi": taux_retour
		})
	# on retourne notre tableau
	return formations
