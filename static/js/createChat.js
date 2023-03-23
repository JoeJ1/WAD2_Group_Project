const memberInput = document.getElementById("memberInput");
const addMemberButton = document.getElementById("addMemberButton");
const memberListInput = document.getElementById("memberListInput");
const members = [];

var usernames = JSON.parse(USERS);
const currentUser = JSON.parse(CURR_USER);
addMemberButton.addEventListener("click", function() {
  const memberName = memberInput.value;
  if (memberName !== "") {
    const user = usernames.find(u => u === memberName);
    if (user) {
      if (members.includes(user)){
        alert(`User ${memberName} is already in the chat.`);
      } 
      else if (user === currentUser) {
        alert(`You cannot add yourself to the chat.`);
      }
      else {
        members.push(user);
        memberInput.value = "";
        renderMembers();
        updateMemberListInput();
      }
  } else {
      alert(`User ${memberName} not found.`);
  }
  }
});

function renderMembers() {
  memberList.innerHTML = "";
  for (let i = 0; i < members.length; i++) {
    const li = document.createElement("li");
    const close = document.createElement("a");
    close.classList.add('btn-close');
    close.classList.add('float-end');
    close.onclick=function(){
        members.splice(i,1);
        renderMembers();
    }
    li.textContent = members[i];
    li.classList.add('list-group-item');
    li.appendChild(close);
    memberList.appendChild(li);
  }
}

function updateMemberListInput() {
  memberListInput.value = JSON.stringify(members);
}
