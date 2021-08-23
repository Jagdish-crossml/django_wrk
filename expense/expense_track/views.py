from expense_track.models import Expense
from django.shortcuts import render, redirect
from .models import Expense
from .forms import *
from django.contrib import messages
# Create your views here.
"""
function to collect data from django form
to post data in db.
"""

def index(request):
    expense_list = Expense.objects.all()
    # if Expense.objects.aggregate(sum('comment') >= 10000):
    #     messages.info(request,'your expenses exceed limit')


    form = ExpenseForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST':
        print(request.POST)

        if form.is_valid():
            # save the form data to model
            form.save()

        return redirect('/')
             
    else:
        context = {'expense_list': expense_list, 'form': form}
        
    return render(request, 'expense_track/ui.html', context)

"""
function to fetch current month entries
"""
def thismonth(request):
	
	this_month = datetime.date.today().strftime("%B")

	this_expenses = Expense.objects.filter(date__month=int(datetime.date.today().strftime("%m")))

	context1 = {'this_expenses':this_expenses,'this_month':this_month}

	return render(request, 'expense_track/cur_month.html',context1)


"""
function to fetch previous month entries
from the database
"""
def prevMonth(request):
	
	month_is = datetime.date(2021,int(datetime.date.today().strftime("%m"))-1, 1).strftime('%B')

	expenses = Expense.objects.filter(date__month=int(datetime.date.today().strftime("%m"))-1)

	context = {'expenses':expenses,'month_is':month_is}

	return render(request, 'expense_track/prev_month.html',context)

def yearly(request):
    year = datetime.date.today().strftime("%Y")
    is_expenses = Expense.objects.filter(date__year=int(datetime.date.today().strftime("%Y")))
    context = {'is_expenses':is_expenses,'year':year}
    return render(request, 'expense_track/cat.html',context)

