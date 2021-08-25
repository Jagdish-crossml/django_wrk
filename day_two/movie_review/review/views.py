from django.forms.forms import Form
from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse 
from .forms import MovieForm
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    
    form = MovieForm(request.POST or None ,request.FILES or None)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/')
    else:
        context = {'movies':movies,'form':form}       
    return render(request,'review/ui.html',context)
