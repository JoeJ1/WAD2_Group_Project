from django import template
from chat.models import Chat

register = template.Library()

@register.inclusion_tag('chat/all_chats.html')
def get_chat_list(request, current_chat=None):
    context_dict = {}
    try:
        chat_list = []
        # for i in Chat.objects.all():
        #     print(i.users.all())
        for chat in Chat.objects.all():
            for user in chat.users.all():
                if str(user) == str(request.user):
                    chat_list.append(chat)
                    break
        context_dict['chats'] = chat_list
        context_dict['current_chat'] = current_chat
    except:
        context_dict['chats'] = None
    return context_dict