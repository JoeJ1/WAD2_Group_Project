import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'MyChatGLA.settings')

import django




if __name__ == '__main__':
    django.setup()
    # import AFTER setup
    from chat.models import UserProfile, Chat, Message, File

from django.contrib.auth.models import User

def populate():


    users = [
        {"username":'Reuben_C',
         "password":'HelloTEST123456',
        "display_name":'Reuben',
         "picture":'/media/logo.png'}

    ]

    user1 = User.objects.create_user('asdsdasw',password='password4545FDKEFp')
    UserProfile.objects.get_or_create(user=user1, display_name='reubenss', picture='/media/logo.png')

populate()