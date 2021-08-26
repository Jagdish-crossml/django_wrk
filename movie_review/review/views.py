from django.forms.forms import Form
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.http import HttpResponse, request
from .forms import *
from .templates import *
from .forms2 import SearchForm
from .forms3 import RatingForm
# from .forms4 import ProjectSettings
# Create your views here.


def index(request):
    movies = Movie.objects.all()

    form = MovieForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/')
    else:
        context = {'movies': movies, 'form': form}
    return render(request, 'review/ui.html', context)

def award_movie(request):
    movies = Award.objects.all()

    form = AwardForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/')
    else:
        context = {'movies': movies, 'form': form}
    return render(request, 'review/awards.html', context)

def artist_movie(request):
    movies = Artist.objects.all()

    form = ArtistForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review/')
    else:
        context = {'movies': movies, 'form': form}
    return render(request, 'review/artist.html', context)


def search_movie(request):
    form = SearchForm(request.POST or None)
    queryset = None
    if request.method == 'POST':
        queryset = Movie.objects.filter(name__icontains=form['name'].value())

    context = {
        "form": form,
        "queryset": queryset}
    return render(request, 'review/search.html', context)


def rate_movie(request):
    rate = Rating.objects.all()
    # vote = Rating.objects.get_or_create('votes')
    # vote.count += 1
    # vote.save()
    form = RatingForm(request.POST or None, request.FILES or None)
    print(form)
    # breakpoint()
    # vote_count =Rating.objects.filter(movie_rating__icontains='10').count()
    # votes = vote_count
    # votes.save()
    new = form.save()
    print(new)
    rate = None
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/review/')
    else:
        context = {'form': form, 'rate': rate}
    return render(request, 'review/rating.html', context)


# def update_project(request, artists):
#     project = None
#     if artists:
#         project = get_object_or_404(Movie, name=artists) # somehow get your project object

#     qs = project.members.all()

#     if request.method == 'POST':
#         form = ProjectSettings(qs, request.POST)
#         if form.is_valid(): # All validation rules pass
#             # Process the data in form.cleaned_data
#             # Movie.summary = form.cleaned_data['summary']
#             Movie.artists = form.cleaned_data['artists']
#             project.save()
#             return redirect('/projects/' + Movie.artists + '/')
#     else:
#         form = ProjectSettings(qs)

#     return render('', {'form': form}, context_instance=RequestContext(request))
