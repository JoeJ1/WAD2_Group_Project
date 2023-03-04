import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'MyChatGLA.settings')

import django








def populate():


    users = [
        {"username":'Reuben_C',
         "password":'HelloTEST123456',
        "display_name":'Reuben',
         "picture":'/media/logo.png'},

        {"username":'Onur_H',
         "password":'HelloTEST123456',
         "display_name":'Onur',
         "picture":'/media/logo.png'},

        {"username":'Joe_F',
         "password":'HelloTEST123456',
         "display_name":'Joe',
         "picture":'/media/logo.png'},

        {"username":'Lewis_S',
         "password":'HelloTEST123456',
         "display_name":'Lewis',
         "picture":'/media/logo.png'},

        {"username":'David_B',
         "password":'HelloTEST123456',
         "display_name":'David',
         "picture":'/media/logo.png'},

        {"username":'James_T',
         "password":'HelloTEST123456',
         "display_name":'James',
         "picture":'/media/logo.png'}

    ]

    chats= [
        {"name":'Wad_Buds',
         "description":'Discussion group for WAD labs',
         "users":'',
         "owner": add_owner_user('Onur_H','HelloTEST123456','Onur','/media/logo.png')
    }


    ]

    for user in users:
        i = 0
        u = add_user(user['username'],user['password'],user['display_name'],user['picture'])
        print(u)
        ++i
        print(i)
        for chat in chats:
            j = 0
            if j == 0:
                c = create_chat(chat['name'],chat['description'],chat['owner'])
            print(j)
            if u:
                c.users.add(u)
            ++j

def add_owner_user(username,password,display_name,picture):
    user_temp = User.objects.create_user(username,password=password)
    u = UserProfile.objects.get_or_create(user=user_temp, display_name=display_name, picture=picture)[0]
    u.save()
    return u
def add_user(username,password,display_name,picture):
    try:
        user_temp = User.objects.create_user(username,password=password)
        u = UserProfile.objects.get_or_create(user=user_temp, display_name=display_name, picture=picture)[0]
        u.save()
        return u
    except:
        return None




def create_chat(name,description,owner):
    c = Chat.objects.get_or_create(name=name,description=description,owner=owner)[0]
    c.save()
    return c

if __name__ == '__main__':
    django.setup()
    # import AFTER setup
    from chat.models import UserProfile, Chat, Message, File
    from django.contrib.auth.models import User
    populate()