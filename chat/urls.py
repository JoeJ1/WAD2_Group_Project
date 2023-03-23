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
    path('search_profiles/', views.search_profiles, name='search_profiles'),
    path('profile/', views.profile, name='profile'),
    path('test/', views.test, name='test'),
    path('chatroom/<slug:chat_name_slug>/', views.chat, name='chatroom'),
    path('chatroom/<slug:chat_name_slug>/leave', views.leave_group_chat, name='leave'),
    path('chatroom/<slug:chat_name_slug>/members', views.members, name='members'),
    path('chatroom/<slug:chat_name_slug>/files', views.files, name='files'),
    path('chatroom/<slug:chat_name_slug>/delete', views.delete_group_chat, name='delete'),
    path('chat/profile/delete_account', views.delete_account, name='delete_account'),
    path('chatroom/<slug:chat_name_slug>/get_messages', views.get_messages, name='get_messages'),
    path('chatroom/<slug:chat_name_slug>/send_message', views.send_message, name='send_message'),
    path('chatroom/<slug:chat_name_slug>/remove_member/<str:username>', views.remove_member, name='remove_member'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
