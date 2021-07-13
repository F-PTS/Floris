from django.urls import path

from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name='register'),
    path('addflower/', views.AddPlantView, name='addflower'),
    path('index.html', views.logout_view, name='logout'),
    path('workspace/', views.workspaceView.as_view(), name='workspace'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    
]