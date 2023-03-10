from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from chat.models import Chat, File, UserProfile, Message
from chat.forms import UserForm, UserProfileForm

# def get_user_chats(request):
#     context_dict = {}
#     try:
#         chat_list = []
#         # for i in Chat.objects.all():
#         #     print(i.users.all())
#         for chat in Chat.objects.all():
#             for user in chat.users.all():
#                 if str(user) == str(request.user):
#                     chat_list.append(chat)
#                     break
#         context_dict['chats'] = chat_list
#     except:
#         context_dict['chats'] = None
#     return context_dict

#  idk if i still need this so dont delete

def chat(request, chat_name_slug):
    chat_list = Chat.objects.all()
    context_dict = {}
    context_dict['chats'] = chat_list
    return render(request, 'chat/chat.html', context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('chat:chat'))
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")  #needs changed to handle wrong logins
    else:
        return render(request, "chat/login.html", context={})
    
def main_page(request):
    return render(request, "chat/mainpage.html", context={})

def profile(request):
    pass

def send_message(request, message):
    pass

def check_messages(request):
    pass

def sign_up(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture  = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'chat/SignUp.html',
                  context={'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered}
                  )#request needs to be added


def create_page(request):
    return render(request,'chat/CreateChat.html',context={})

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('chat:login'))#need to add a reverse url

def test(request):
    return render(request,'chat/test.html',context = {})

def profile(request):
    return render(request,'chat/Profile.html',context={})
