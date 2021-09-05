from django.db.models.query import QuerySet
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Document
from django.utils import timezone
from django.template.defaultfilters import filesizeformat
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# class DocumentViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes=(TokenAuthentication,)
#     serializer_class = DocumentSerializer
#     queryset = Document.objects.all()

    


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def docList(request):
	# breakpoint()
	docList  = Document.objects.filter(user=request.user)

	serializer = DocumentSerializer(docList, many=True)

	return Response(serializer.data)
#     else:
        
#         doc_obj = Document.objects.all()
#         ser_obj = DocumentSerializer(doc_obj, many=True)

#         return Response(ser_obj.data)


# class FileView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def put(self, *args, **kwargs):
#         file_serializer = DocumentSerializer(data=request.data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)


# @login_required
# def index(request):
#     docs = Document.objects.all()
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         user = request.user.username
#         u_obj = User.objects.get(username=user)
#         total = Document.objects.filter(
#             user=u_obj.pk).filter(date__date=timezone.now())
#         this_day = total.count()
#         print(this_day)
#         if this_day == 5:
#             messages.info(request, "You can Only upload 5 docs/day !")
#             return redirect('/index/')
#         else:
#             if form.is_valid():
#                 if request.FILES['PDF'].size > 5242880:
#                     messages.info(request, "Size can't be more than 5 MiB")
#                     return redirect('/index/')
#                 else:
#                     obj = form.save(commit=False)
#                     obj.user = u_obj
#                     obj.save()
#                     return redirect('/index/')

#     else:
#         form = DocumentForm()
#     return render(request, 'registration/upload.html', {
#         'form': form, 'docs': docs
#     })


# @login_required
# def search_doc(request):
#     form = SearchForm(request.POST or None)
#     queryset = None
#     if request.method == 'POST':
#         queryset = Document.objects.filter(name__icontains=form['name'].value(
#         ))

#         print(queryset)
#     context = {
#         "form": form,
#         "queryset": queryset}
#     return render(request, 'registration/search.html', context)


# @login_required
# def date_sort(request):
#     """
#     function to sort movies within a range of date
#     """
#     if request.POST:
#         from_date = request.POST['from_date']
#         to_date = request.POST['to_date']
#         # breakpoint()
#         docs = Document.objects.filter(date__range=[from_date, to_date])
#         context = {'docs': docs}
#     else:
#         docs = Document.objects.none()
#         context = {'docs': docs}
#     return render(request, 'registration/date_sort.html', context)


# def sort_name(request):
#     name_sort = Document.objects.filter(user=2 or 3).order_by('name')
#     return render(request, 'registration/srt_name.html', {'name_sort': name_sort})


# @login_required
# def rep(request):
#     user_docs = Document.objects.filter(
#         user=User.objects.get(username=request.user.username))
#     daily_uploads = user_docs.filter(date__day=timezone.now().strftime("%d"))
#     daily = daily_uploads.count()
#     monthly_uploads = user_docs.filter(
#         date__month=timezone.now().strftime("%m"))
#     monthly = monthly_uploads.count()
#     yearly_uploads = user_docs.filter(date__year=timezone.now().strftime("%Y"))
#     yearly = yearly_uploads.count()

#     list = None
#     if 'month' in request.GET:
#         list = user_docs.filter(date__month=request.GET['month'])
#     elif 'year' in request.GET:
#         list = user_docs.filter(date__year=request.GET['year'])

#     return render(request, 'registration/sort.html', {'daily': daily, 'monthly': monthly, 'yearly': yearly, 'pdf_list': list})
