let messages;

$(document).ready(function() {
    updateMessages();
    window.setInterval(updateMessages, 1000);
    $("#send-button").click(getMessages);
    m = document.getElementById("messageListContainer");
    m.scrollTop = m.scrollHeight;
});

function getMessages() {
    let message_input = $("#message-input");
    let content = message_input.val();
    if(message_input.val().length>0) {
        $.get('send_message', {'content':content,'username':username,'chat_slug':slug}, updateMessages);
    }
    message_input.val('');
    m = document.getElementById("messageListContainer");
    m.scrollTop = m.scrollHeight;
}

function createMessage(sender,content,pic) {
    let m_container = document.createElement("div");
    let m_card = document.createElement("div");
    let m = document.createElement("div");
    let m_title = document.createElement("h5");
    let m_body = document.createElement("p");
    let m_img = document.createElement("img");

    if(sender==username) {
        m_container.classList.add('justify-content-end');
        m_card.classList.add('align-items-end', 'bg-primary', 'text-light');
        m_card.style.borderTopRightRadius=0;
        m_body.classList.add('text-end');
        m_title.classList.add('align-items-end', 'text-end');
    } else {
        m_card.style.borderTopLeftRadius=0;
        m_card.classList.add('bg-secondary', 'text-light');
    }

    m_container.classList.add('w-100', 'container', 'd-inline-flex', 'pb-2');
    m_card.classList.add('card', 'mw-50');
    m.classList.add('card-body');
    m_title.classList.add('card-title');
    m_body.classList.add('card-text', 'me-5', 'ms-5');
    m_img.classList.add('rounded-circle')
    m_img.width=50;
    m_img.height=50;

    m_img.src=pic;
    m_body.textContent=content;
    
    if(sender==username) {
        m_title.appendChild(document.createTextNode(sender));
        m_title.appendChild(m_img);
        m_img.classList.add('ms-2');
    } else {
        m_title.appendChild(m_img);
        m_title.appendChild(document.createTextNode(sender));
        m_img.classList.add('me-2');
    }

    m.appendChild(m_title);
    m.appendChild(m_body);
    m_card.appendChild(m);
    m_container.appendChild(m_card);
    return(m_container);
}

function updateMessages() {
    $.get('get_messages',
        {'chat_slug':slug},
        function(data) {
            let messages = JSON.parse(data);
            let messagesList = $("#messagesList");
            messagesList.empty();
            for(let i=0; i < messages.length; i++) {
                messagesList.append(createMessage(messages[i].sender,messages[i].content, messages[i].pic));
            }
        });
}
