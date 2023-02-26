from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat, name='chat'),
    path('profile/', views.profile, name='profile'),
    path('auth/login/', views.login, name='login'),
    path('auth/logout/', views.user_logout, name='logout'),
]
