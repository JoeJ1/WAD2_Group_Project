import json
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from chat.models import Chat, File, UserProfile, Message, DjangoUser
from chat.forms import ChangeUserDisplayName, FileForm, UserForm, UserProfileForm, ChatForm, ChangeUserProfilePic


@login_required
def search_profiles(request):
    context_dict = {}
    
    if request.method == "POST":
        searched = request.POST['searched']
        profiles = UserProfile.objects.filter(display_name__contains=searched)
        context_dict['searched'] = searched
        context_dict['profiles'] = profiles
        return render(request, 'chat/search_profiles.html', context_dict)
    else:
        return render(request, 'chat/search_profiles.html', context_dict)
        

@login_required
def leave_group_chat(request, chat_name_slug):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        chat = Chat.objects.get(slug=chat_name_slug)
    except Chat.DoesNotExist:
        chat = None
    chat.users.remove(user_profile)
    chat.save()
    return redirect(reverse('chat:chat'))


@login_required
def get_user_chats(request):
    context_dict = {}
    try:
        chat_list = []
        for chat in Chat.objects.all():
            for user in chat.users.all():
                if str(user) == str(request.user):
                    chat_list.append(chat)
                    break
        context_dict['chats'] = chat_list
    except:
        context_dict['chats'] = None
    return context_dict

@login_required
def members(request, chat_name_slug):
    context_dict = {}
    try:
        chat = Chat.objects.get(slug=chat_name_slug)
        chat_members = Chat.objects.get(slug=chat_name_slug).users.all()
        chat_owner = chat.owner
        user = UserProfile.objects.filter(user=request.user)
        # chat_image = chat.image #could someone add this to data base
    except:
        chat = None
        chat_members = None
        chat_owner = None
    context_dict['chat_name'] = chat
    context_dict['chat_members'] = chat_members
    context_dict['chat_name_slug'] = chat_name_slug
    context_dict['owner'] = chat_owner
    context_dict['current_user'] = user.get()
    print(user.get(), chat_owner)
    return render(request, 'chat/members.html', context_dict)

@login_required
def remove_member(request, chat_name_slug, username):
    user = DjangoUser.objects.get(username=username)
    userProfile = UserProfile.objects.get(user=user)
    chat = Chat.objects.get(slug=chat_name_slug)
    chat.users.remove(userProfile)
    chat.save()
    Chat.objects.get(slug=chat_name_slug).users.remove(userProfile)
    return redirect(reverse('chat:members', args=(chat_name_slug,)))


@login_required
def add_member(request, chat_name_slug, username):
    try:
        user = DjangoUser.objects.get(username=username)
    except:
        return redirect(reverse('chat:members', args=(chat_name_slug,)))
    userProfile = UserProfile.objects.get(user=user)
    chat = Chat.objects.get(slug=chat_name_slug)
    chat.users.add(userProfile)
    chat.save()
    return redirect(reverse('chat:members', args=(chat_name_slug,)))

@login_required
def delete_account(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        user = DjangoUser.objects.get(userprofile=user_profile)
    except UserProfile.DoesNotExist:
        user = None
    user_profile.delete()
    user.delete()
    return redirect(reverse('chat:signup'))

@login_required
def delete_group_chat(request, chat_name_slug):
    try:
        chat = Chat.objects.get(slug=chat_name_slug)
    except Chat.DoesNotExist:
        chat = None
    chat.delete()
    return redirect(reverse('chat:chat')) 

@login_required
def files(request, chat_name_slug):
    context_dict = {}
    form = FileForm
    context_dict['form'] = form
    try:
        chat = Chat.objects.get(slug=chat_name_slug)
        user = UserProfile.objects.filter(user=request.user)
        chat_owner = chat.owner
    except:
        chat = None
        user = None
    context_dict['chat_name_slug'] = chat_name_slug
    context_dict['chat_name'] = chat
    context_dict['current_user'] = user.get()
    context_dict['owner'] = chat_owner
    context_dict['files'] = File.objects.filter(chat=chat)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid form')
            
            file_instance = form.save(commit=False)
            file_instance.chat = chat 
            
            file_instance.save()
            return redirect(reverse('chat:files', kwargs={'chat_name_slug': chat_name_slug}))
        else:
            print(form.errors)
    else:
        form = FileForm()
    return render(request, 'chat/files.html', context_dict)

@login_required
def chat(request, chat_name_slug):
    context_dict = {}
    context_dict['chats'] = Chat.objects.all()
    try:
        this_chat = Chat.objects.get(slug=chat_name_slug)
        owner = this_chat.owner
        context_dict['messages'] = Message.objects.filter(chat=this_chat)
        context_dict['owner'] = owner
        context_dict['chat_name'] = this_chat.name
        context_dict['chat_name_slug'] = this_chat.slug
        context_dict['current_user'] = UserProfile.objects.filter(user=request.user).get()
        context_dict['this_username'] = UserProfile.objects.filter(user=request.user)[0].user.username
    except Chat.DoesNotExist:
        chat = None
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
            return render(request, "chat/login.html", context={'invalid_login':True})
    else:
        return render(request, "chat/login.html", context={'invalid_login':False})

@login_required
def main_page(request):
    return render(request, "chat/mainpage.html", context=get_user_chats(request))

#@login_required
def send_message(request, chat_name_slug):
    username = request.GET['username']
    content = request.GET['content']
    chat_slug = request.GET['chat_slug']
    chat = Chat.objects.get(slug=chat_slug)
    sender = UserProfile.objects.get(user=request.user)
    if(content):
        m = Message.objects.create(content=content, chat=chat, sender=sender)
        m.save()
    return get_messages(request, chat_name_slug)

#@login_required
def get_messages(request, chat_name_slug):
    chat_slug = request.GET['chat_slug']
    messages = Message.objects.filter(chat=Chat.objects.get(slug=chat_slug))
    messages_list = [{'pic':m.sender.picture.url,'time_stamp':str(m.time_stamp), 'sender':m.sender.user.username, 'content':m.content} for m in messages]
    return HttpResponse(json.dumps(messages_list))

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
            return redirect(reverse('chat:login'))
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'chat/signup.html',
                  context={'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered}
                  )#request needs to be added

@login_required
def create_page(request):
    context_dict = {}
    user_profiles = UserProfile.objects.all()
    usernames = [i.user.username for i in user_profiles]
    context_dict['all_users'] = user_profiles
    context_dict['usernames'] = json.dumps(usernames)
    context_dict['current_user'] = json.dumps(request.user.username)
    
    if request.method == 'POST':
        members_str = request.POST.get('user_list')
        try:
            members = json.loads(members_str)
        except:
            members = []
        owner = UserProfile.objects.get(user=request.user)
        chat_form = ChatForm(request.POST, request.FILES)
        user_list = []
        for i in user_profiles:
            if i.user.username in members:
                user_list.append(i)

        if chat_form.is_valid():
            print('valid')
            chat = chat_form.save(commit=False)
            chat.save()
            chat.users.add(owner)
            for i in user_list:
                chat.users.add(i)
            chat.save()
            return redirect('chat:chat')
        else:
            print(chat_form.errors)
    else:
        chat_form = ChatForm()
        
    return render(request,'chat/createchat.html',context=context_dict)

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('chat:login'))#need to add a reverse url

def test(request):
    return render(request,'chat/test.html',context = {})

@login_required
def profile(request):
    context_dict = {}
    pic_form = ChangeUserProfilePic
    display_name_form = ChangeUserDisplayName
    try:
        context_dict['display_name_form'] = display_name_form
        context_dict['pic_form'] = pic_form
        context_dict['current_user'] = UserProfile.objects.filter(user=request.user).get()
    except:
        context_dict['current_user'] = None
        
    if request.method == 'POST':
        
        
        user = UserProfile.objects.get(user=request.user)
        form_type = request.POST.get('form_type')
        if form_type == 'display_name_form':
            display_name_form = ChangeUserDisplayName(request.POST)
            if display_name_form.is_valid():
                print('valid display')
                display_name = display_name_form.cleaned_data['display_name']
                user.display_name = display_name
                user.save()
                return redirect('chat:profile')
                # handle display_name_form submission
            else:
                print(display_name_form.errors)
        elif form_type == 'pic_form':
            pic_form = ChangeUserProfilePic(request.POST, request.FILES)
            if pic_form.is_valid():
                print('valid')
                picture = pic_form.cleaned_data['picture']
                user.picture = picture
                user.save()
                return redirect('chat:profile')
            else:
                print(pic_form.errors)
    else:
        display_name_form = ChangeUserDisplayName()
        pic_form = ChangeUserProfilePic()

        
    return render(request,'chat/profile.html',context=context_dict)
