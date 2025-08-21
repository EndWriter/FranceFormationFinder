from rest_framework.views import APIView
from rest_framework.response import Response
from .scraper import scrape_france_travail

class FormationSearchView(APIView):
	def get(self, request):
		keyword = request.GET.get("keyword", "")
		results = scrape_france_travail(keyword)
		return Response(results)
