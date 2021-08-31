from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_doc/', views.search_doc, name='search'),
    path('date_sort/', views.date_sort, name='date'),
]