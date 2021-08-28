from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('search_movie/',views.search_movie,name="search_movie"),
    path('rate_movie/',views.rate_movie,name="rate_movie"),
    path('award_movie/',views.award_movie,name="Awards"),
    path('artist_movie/',views.artist_movie,name="Artist"),
    path('top/',views.top,name="top"),
    path('down/',views.down,name="down"),
    path('date_sort/',views.date_sort,name="sort")

]