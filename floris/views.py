from django.db.models import query
from .models import Flower
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, Http404, request
from .forms import LoginForm, PlantForm, RegisterForm
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from rest_framework.response import Response
from rest_framework import generics
from .serializers import FlowerSerializer
# Create your views here.

def index2(request):
    username = ''
    password = ''
    
    
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = request.POST['login']
        #password = form.cleaned_data.get('password')
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #with connection.cursor() as cursor:
                #cursor.execute("SELECT username FROM auth_user WHERE username = %s", [username])
                #row = cursor.fetchone()
            #for x in row:
                #global value
                #value = x
            login(request, user)

            if request.user.is_authenticated:
                return HttpResponseRedirect('')
            else:
                return HttpResponse('Please, log in.')
                
        else:
            return HttpResponseRedirect('/login/')
    else:
        form = LoginForm()
    context = {'form': form, 'username': username}
    return render(request, 'floris/index.html', context)


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():

            return HttpResponseRedirect('')

    else:
            
        form = LoginForm()
        
    return render(request, 'floris/login.html', {'form': form})

def register(request):
    submition = request.POST.get("submit")
    login = ''
    password = ''
    rep_password = ''
    email = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        
        if form.is_valid():
            login = form.cleaned_data.get("login")
            email = form.cleaned_data.get("mail")
            password = form.cleaned_data.get("password")
            rep_password = form.cleaned_data.get("repeated_password")
            if password == rep_password:
                user = User.objects.create_user(login, email, password)       
                return HttpResponseRedirect('/login/')
    else:
        form = RegisterForm()

    context = {'form': form, 'login': login, 'email': email,'password': password, 'rep_password': rep_password}
    
    return render(request, 'floris/register.html', context)


class ProfileView(generic.DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "floris/profile.html"

    def get_object(self):

        object = get_object_or_404(User, username=self.kwargs.get("username"))

        if self.request.user.username == object.username:
            return object
        else:
            print("you are not the owner!!")
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({'username': self.kwargs.get("username")})
        return context


    
def AddPlantView(request):
    plant_name = ''
    water_time = 0
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PlantForm(request.POST, request.FILES)
            if form.is_valid():
                plant_name = form.cleaned_data.get('name')
                water_time = form.cleaned_data.get('water_time')

                u = get_object_or_404(User, username=request.user.username)
                f = Flower(name=plant_name, water_time=water_time, owner_id=u)
                f.save()
                    
                return HttpResponse('Kwiatek wpisany pomyslnie')
        else:
            form = PlantForm()
    else:
        return HttpResponse('niezalogowany')
    return render(request,'floris/addflower.html', {'form': form})

        
def logout_view(request):
    logout(request)

    return HttpResponse('Wylogowano!')

class workspaceView(generics.RetrieveAPIView):
    template_name = 'floris/workspace.html'

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
    

    def get_queryset(self):
        print("XDDDDDDDDDDD")
        print(self.request.user.id)
        return Flower.objects.filter(owner_id=self.request.user.id)
        
    
    def get(self, request, **kwargs):
        #if request.user.is_authenticated:
            queryset = self.get_queryset()
            #resp = super().get(request, **kwargs)
            serializer = FlowerSerializer(queryset, many=True)
            return Response(serializer.data)
        #else:
            #return HttpResponse('niezalogowany')
    
    def get_context_data(self, **kwargs):
        context =  super(workspaceView, self).get_context_data(**kwargs)
        return context
        