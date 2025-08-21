from rest_framework.views import APIView
from rest_framework.response import Response
from .scraper import scrape_france_travail
from django.shortcuts import render

class FormationSearchView(APIView):
	def get(self, request):
		keyword = request.GET.get("keyword", "")
		results = scrape_france_travail(keyword)
		return Response(results)

# retourne notre template (page de recherche)
def search_page(request):
    return render(request, 'formations/search.html')
