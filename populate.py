import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'MyChatGLA.settings')
import django

def populate():


    users = {"Reuben":add_user('Reuben_S','1234','Reuben','/uploadpics/logo.png'),

        "Onur":add_user('Onur_C','1234','Onur','/uploadpics/logo.png'),

        "Joe":add_user('Joe_J','1234','Joe','/uploadpics/logo.png'),

        "Lewis":add_user('Lewis_B','1234','Lewis','/uploadpics/logo.png'),

        "David":add_user('David_M','1234','David','/uploadpics/logo.png'),

        "James":add_user('James_M','1234','James','/uploadpics/logo.png')}


    chats= [
        {"name":'WAD Group 11C',
         "description":'Discussion for the WAD2 group project',
         "users":'',
         "owner": users["Onur"],
         "image":'/chat_images/rango.jpg'},

        {"name":'Maths 2C',
         "description":'Groupchat for help with real analysis',
         "users":'',
         "owner": users["Joe"],
         "image":'/chat_images/logo.png'},

        {"name":'OOSE',
         "description":'Post your OOSE questions here!',
         "users":'',
         "owner": users["Lewis"],
         "image":'/chat_images/rango.jpg'},

        {"name":'Django discussion',
         "description":'Get help on django problems!',
         "users":'',
         "owner": users["David"],
         "image":'/chat_images/logo.png'},
    ]

    messages = [
        {'chat':'WAD Group 11C',
         'sender':'Onur_C',
         'content':'Hello!'},
        {'chat':'Maths 2C',
         'sender':'Reuben_S',
         'content':'Hi!'},
        {'chat':'OOSE',
         'sender':'Lewis_B',
         'content':'12345678'},
        {'chat':'Django discussion',
         'sender':'Joe_J',
         'content':'12345678'},
        {'chat':'Django discussion',
         'sender':'David_M',
         'content':'910111213'},
        {'chat':'Maths 2C',
         'sender':'James_M',
         'content':'19579825985198'},
    ]

    files = [
        {"name":'TestFile1',
         "data":'/uploadpics/test/rango.jpg',
         "chat":'WAD Group 11C'},
        {"name":'TestFile1',
         "data":'/uploadpics/logo.jpg',
         "chat":'Maths 2C'},
        {"name":"TestFile2",
         "data":'/uploadpics/rango.jpg',
         "chat":'OOSE'},
        {"name": "TestFile1",
         "data": '/uploadpics/logo.jpg',
         "chat": 'Django discussion'},
        {"name": "TestFile5",
         "data": '/uploadpics/rango.jpg',
         "chat": 'Maths 2C'}
    ]

    for chat in chats:
        c = create_chat(chat['name'],chat['description'],chat['owner'], chat['image'])
        for user in users:
            c.users.add(users[user])

    for message in messages:
        add_message(message['sender'],message['chat'],message['content'])
    
    for file in files:
        add_file(file['data'],file['chat'])
    #chat = Chat.objects.filter(name = "Wad_Buds")[0]
    #f = File.objects.get_or_create(name="Hello", data="/uploadpics/logo.png", chat=chat)[0]
    #f.save()
def add_file(data,chat_name):
    chat = Chat.objects.filter(name = chat_name)[0]
    f = File.objects.get_or_create( data = data, chat = chat)[0]
    f.save()
    return f
def add_user(username,password,display_name,picture):
    try:
        user_temp = User.objects.create_user(username,password=password)
        u = UserProfile.objects.get_or_create(user=user_temp, display_name=display_name, picture=picture)[0]
        u.save()
        return u
    except:
        return None

def add_message(sender_username, chat_name, content):
    s = UserProfile.objects.get(user=User.objects.get(username=sender_username))
    c = Chat.objects.get(name=chat_name)
    m = Message.objects.create(content=content, chat=c, sender=s)
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
    from django.contrib.sites.models import Site
    from allauth.socialaccount.models import SocialApp
    from allauth.socialaccount.providers.google import provider
    populate()
    print("DB populated")
    obj = Site.objects.get(id=1)
    obj.domain="https://mychatgla.pythonanywhere.com"
    obj.name="https://mychatgla.pythonanywhere.com"
    obj.save()
    socialApp = SocialApp.objects.create(name = "GroupProject", client_id="992328428322-5dabhp72ve3ot8slfrgdu3t6hcn0775f.apps.googleusercontent.com", secret="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")
    socialApp.sites.set([obj])

