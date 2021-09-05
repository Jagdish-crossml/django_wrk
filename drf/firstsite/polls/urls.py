from os import name
from django.urls import path,include
from rest_framework import routers
from . import views
from .views import DocumentViewSet


router = routers.DefaultRouter()
router.register(r'DocumentViewSet', views.DocumentViewSet,basename='DocumentViewSet')

urlpatterns = [
    # path('', views.index, name='index'),
    # path('search_doc/', views.search_doc, name='search'),
    # path('date_sort/', views.date_sort, name='date'),
    # path('rep/', views.rep, name='sort'),
    # path('sort_name/', views.sort_name, name='sort_name'),
    path('DocumentViewSet/', include(router.urls)),
    # path('api_index/', views.apiIndex, name="api_index"),
    # path('FileView/',views.FileView.as_view(),name='FileView'),
    # path('hello/',views.HelloView.as_view(),name='hello'),

]