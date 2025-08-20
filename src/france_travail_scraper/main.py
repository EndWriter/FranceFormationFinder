# Mon interface
import sys
import json

def main():
	# on vérifie que l'utilisateur a fourni un mot-clé
	if len(sys.argv) < 2:
		print("Usage: python -m france_travail_scraper.main <mot-clé>")
		sys.exit(1)
	keyword = sys.argv[1]
	# Pour l'instant, on retourne un JSON vide
	result = {"Recherche": keyword, "formations": []}
	# vu que l'on retourne un JSON, on rends le rendu plus lisible
	print(json.dumps(result, ensure_ascii=False, indent=2))
    
if __name__ == "__main__":
	main()
