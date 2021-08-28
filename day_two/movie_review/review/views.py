from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .templates import *
from django.urls import reverse
from django.db.models import Avg
from django.contrib import messages
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
        queryset = Movie.objects.filter(name__icontains=form['name'].value(
        )) or Movie.objects.filter(artists__aname=form['name'].value())
        print(queryset)
    context = {
        "form": form,
        "queryset": queryset}
    return render(request, 'review/search.html', context)


def rate_movie(request):
    """
    function to rate Movies
    """

    if request.method == "POST":
        rate_form = RatingForm(request.POST)
        # print(type(rate_form))
        if rate_form.is_valid():
            form_object = rate_form.save(commit=False)
            form_object.movie = rate_form.cleaned_data.get('movie')
            form_object.movie_rating = rate_form.cleaned_data['movie_rating']

            filtered_data = Rating.objects.filter(
                movie=form_object.movie, movie_rating=form_object.movie_rating)

            if filtered_data.count() >= 1:
                rate_obj = filtered_data.get()
                rate_obj.votes += 1
                rate_obj.save()
                # set_avg_rating(form_object.movie)
            else:
                form_object.votes = 1
                form_object.save()
                form_object.movie.save()
                # set_avg_rating(form_object.movie)
            movie = Movie.objects.get(name=form_object.movie)
            rating_obj = Rating.objects.filter(movie=movie)
            rating_list = [int(rating_data.votes)*int(rating_data.movie_rating)
                           for rating_data in rating_obj]
            vote_list = [rating_data.votes for rating_data in rating_obj]

            movie.avg_rating = sum(rating_list)/sum(vote_list)

            movie.save()
            messages.success(request, "Rated Successfully !")
            # TODO -> Average rating Logic
            return redirect(reverse('rate_movie'))
        else:
            messages.error(request, "Error While Rating ")
            return redirect(reverse('rate_movie'))

    else:
        rate_form = RatingForm()
        context = {'form': rate_form}
        return render(request, 'review/rating.html', context)


def top(request):
    avrage = Movie.objects.all().order_by('avg_rating')

    return render(request, 'review/order.html', {"context": avrage})


def down(request):
    avrage = Movie.objects.all().order_by('-avg_rating')

    return render(request, 'review/order.html', {"context1": avrage})


def date_sort(request):
    """
    function to sort movies within a range of date
    """
    if request.POST:
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        # breakpoint()
        movies = Movie.objects.filter(release_date__range=[from_date, to_date])
        context = {'movies': movies}
    else:
        movies = Movie.objects.none()
        context = {'movies': movies}
    return render(request, 'review/date_sort.html', context)
