import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'MyChatGLA.settings')
import django

def populate():


    users = {"Reuben":add_user('Reuben_C','HelloTEST123456','Reuben','/uploadpics/logo.png'),

        "Onur":add_user('Onur_H','HelloTEST123456','Onur','/uploadpics/logo.png'),

        "Joe":add_user('Joe_F','HelloTEST123456','Joe','/uploadpics/logo.png'),

        "Lewis":add_user('Lewis_S','HelloTEST123456','Lewis','/uploadpics/logo.png'),

        "David":add_user('David_B','HelloTEST123456','David','/uploadpics/logo.png'),

        "James":add_user('James_T','HelloTEST123456','James','/uploadpics/logo.png')}


    chats= [
        {"name":'Wad_Buds',
         "description":'Discussion group for WAD labs',
         "users":'',
         "owner": users["Onur"],
         "image":'/uploadpics/rango.jpg'},

        {"name":'The Brotherhood',
         "description":'Secret cult meeting',
         "users":'',
         "owner": users["Joe"],
         "image":'/uploadpics/rango.jpg'}
    ]

    messages = [
        {'chat':'Wad_Buds',
         'sender':'Onur_H',
         'content':'Hello!'},
        {'chat':'Wad_Buds',
         'sender':'Reuben_C',
         'content':'Hi! 123'},
        {'chat':'Wad_Buds',
         'sender':'Lewis_S',
         'content':'12345678'},
        {'chat':'The Brotherhood',
         'sender':'Joe_F',
         'content':'12345678'},
        {'chat':'The Brotherhood',
         'sender':'David_B',
         'content':'910111213'},
        {'chat':'The Brotherhood',
         'sender':'James_T',
         'content':'19579825985198'},
    ]

    for chat in chats:
        c = create_chat(chat['name'],chat['description'],chat['owner'], chat['image'])
        for user in users:
            c.users.add(users[user])

    for message in messages:
        add_message(message['sender'],message['chat'],message['content'])

def add_user(username,password,display_name,picture):
    try:
        user_temp = User.objects.create_user(username,password=password)
        u = UserProfile.objects.get_or_create(user=user_temp, display_name=display_name, picture=picture)[0]
        u.save()
        return u
    except:
        return None

def add_message(sender_username, chat_name, content):
    s = UserProfile.objects.filter(user=User.objects.filter(username=sender_username)[0])[0]
    c = Chat.objects.filter(name=chat_name)[0]
    m = Message.objects.get_or_create(content=content, chat=c, sender=s)[0]
    m.save()
    return m

def create_chat(name,description,owner,image):
    c = Chat.objects.get_or_create(name=name,description=description,owner=owner, image=image)[0]
    c.save()
    return c

#def create_message()

if __name__ == '__main__':
    os.system('pip install -r requirements.txt')
    django.setup()
    for f in os.listdir('.'):
        if f.endswith('.sqlite3'):
            os.remove(f)
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'makemigrations'])
    execute_from_command_line(['manage.py', 'migrate'])
    from django.contrib.auth.models import User
    User.objects.create_superuser('root', '', 'root')
    # import AFTER setup
    from chat.models import UserProfile, Chat, Message, File
    from django.contrib.auth.models import User
    from django.template.defaultfilters import slugify
    populate()
    print("DB populated")
