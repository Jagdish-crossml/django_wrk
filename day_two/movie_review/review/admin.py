from django.contrib import admin
from .models import Artist,Award,Movie,Rating
# Register your models here.
admin.site.register(Award),
admin.site.register(Artist),
admin.site.register(Movie),
admin.site.register(Rating)