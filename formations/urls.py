from django.urls import path
from .views import FormationSearchView

urlpatterns = [
    path('search/', FormationSearchView.as_view(), name='formation-search'),
]
