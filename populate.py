import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'MyChatGLA.settings')

import django








def populate():


    users = {"Reuben":add_user('Reuben_C','HelloTEST123456','Reuben','/media/logo.png'),

        "Onur":add_user('Onur_H','HelloTEST123456','Onur','/media/logo.png'),

        "Joe":add_user('Joe_F','HelloTEST123456','Joe','/media/logo.png'),

        "Lewis":add_user('Lewis_S','HelloTEST123456','Lewis','/media/logo.png'),

        "David":add_user('David_B','HelloTEST123456','David','/media/logo.png'),

        "James":add_user('James_T','HelloTEST123456','James','/media/logo.png')}


    chats= [
        {"name":'Wad_Buds',
         "description":'Discussion group for WAD labs',
         "users":'',
         "owner": users["Onur"]},

        {"name":'The Brotherhood',
         "description":'Secret cult meeting',
         "users":'',
         "owner": users["Joe"]}
    ]

    for chat in chats:
        c = create_chat(chat['name'],chat['description'],chat['owner'])
        for user in users:
            if users[user] != chat['owner']:#This can be changed depending on the implementation down the line this exludes the owner to be added as used
                c.users.add(users[user])


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
    #c.slug = slugify(name)
    c.save()
    return c

#def create_message()

if __name__ == '__main__':
    django.setup()
    # import AFTER setup
    from chat.models import UserProfile, Chat, Message, File
    from django.contrib.auth.models import User
    from django.template.defaultfilters import slugify
    populate()
    print("DB populated")
