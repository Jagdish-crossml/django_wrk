from expense_track.models import Expense
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Expense,Category 
from .forms import *
# Create your views here.
def index(request):
    expense_list = Expense.objects.all()
    
    form = ExpenseForm()
    form1 = ChoiceField()

    if request.method == 'POST':
        print(request.POST)

        title = request.POST.get('title')
        Expense(name=title).save()
        
        choice = request.POST.get('choice1')
        Category(cat_name=choice).save()      
        contexty = {'form1':form1}

        return redirect('/')

    else:
        context = {'expense_list' : expense_list,'form':form}
    return render(request,'expense_track/ui.html',context)
           



def category(request):
    category_list = Category.objects.all()
    if request.method == 'GET':
       context1 = {'category_list':category_list}

       return render(request,'expense_track/cat.html',context1)    

