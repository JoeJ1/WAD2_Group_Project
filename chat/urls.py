from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from chat import views

app_name = 'chat'

urlpatterns = [
    path('', views.main_page, name='chat'),
    path('create/', views.create_page, name='create'),
    path('auth/login/', views.user_login, name='login'),
    path('auth/logout/', views.user_logout, name='logout'),
    path('auth/signup/', views.sign_up, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('test/', views.test, name='test'),
    path('chatroom/<slug:chat_name_slug>/', views.chat, name='chatroom'),
]
