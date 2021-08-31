from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Document
from django.utils import timezone



def index(request):
    docs = Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        user = request.user.username
        u_obj = User.objects.get(username=user)
        total = Document.objects.filter(
            user=u_obj.pk).filter(created_at__date=timezone.now())
        this_day = total.count()
        print(this_day)
        if this_day == 5:
            messages.info(request, "You can Only upload 5 docs/day !")
            return redirect('/index/')
        else:
            if form.is_valid():

                obj = form.save(commit=False)
                obj.user = u_obj
                obj.save()
                return redirect('/index/')

    else:
        form = DocumentForm()
    return render(request, 'registration/upload.html', {
        'form': form, 'docs': docs
    })


def search_doc(request):
    form = SearchForm(request.POST or None)
    queryset = None
    if request.method == 'POST':
        queryset = Document.objects.filter(name__icontains=form['name'].value(
        ))
        print(queryset)
    context = {
        "form": form,
        "queryset": queryset}
    return render(request, 'registration/search.html', context)


def date_sort(request):
    """
    function to sort movies within a range of date
    """
    if request.POST:
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        # breakpoint()
        docs = Document.objects.filter(created_at__range=[from_date, to_date])
        context = {'docs': docs}
    else:
        docs = Document.objects.none()
        context = {'docs': docs}
    return render(request, 'registration/date_sort.html', context)

