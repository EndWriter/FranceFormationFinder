from django.urls import path
from .views import FormationSearchView, search_page

urlpatterns = [
    path('search/', FormationSearchView.as_view(), name='formation-search'),
    # Interface de recherche (notre front)
    path('interface/', search_page, name='formation-interface'),
]
