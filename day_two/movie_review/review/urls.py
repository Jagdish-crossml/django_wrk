from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    # path('prevMonth/',views.prevMonth,name="previous"),
    # path('thismonth/',views.thismonth,name="current"),
    # path('yearly/',views.yearly,name="year")
]