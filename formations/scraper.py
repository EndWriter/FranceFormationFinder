import requests
from bs4 import BeautifulSoup

def parse_formations(html):
    soup = BeautifulSoup(html, 'html.parser')
    # on initialise formation comme un tableau vide
    formation = []
    # pour chaque formation qui compose le html
    # on vient cibler les éléments que l'on souhaite extraire
    for li in soup.select('ul.result-list li.result'):
        # titre 
        a_tag = li.select_one('h2.t4.media-heading a')
        title = a_tag.get_text(strip=True) if a_tag else None
        # description
        description_tag = li.select_one('p.description')
        description = description_tag.get_text(strip=True) if description_tag else None
        # Lieu
        subtext_tag = li.select_one('p.subtext')
        lieu = None
        if subtext_tag:
            spans = subtext_tag.find_all('span')
            if spans:
                lieu = spans[-1].get_text(strip=True)
        # le type de formation
        type_tag = li.select_one('p.type')
        type_formation = type_tag.get_text(strip=True) if type_tag else None
        # Durée et date
        time_tag = li.select_one('p.time')
        time = time_tag.get_text(strip=True) if time_tag else None
        # le taux de retour à l'emploi
        rate_tag = li.select_one('p.rate.rate-with-border span.rate-value')
        taux_retour = rate_tag.get_text(strip=True) if rate_tag else None

        # on vient ajouter sous forme d'objet nos formations
        formation.append({
            'title': title,
            'description': description,
            'lieu': lieu,
            'type': type_formation,
            'time': time,
            'taux_retour': taux_retour
        })
    return formation

def scrape_france_travail(keyword):
    url = f"https://candidat.francetravail.fr/formations/recherche?quoi={keyword}&range=0-9&tri=0"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    return parse_formations(response.text)
