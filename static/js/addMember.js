function addMember() {
    let memberName = document.getElementById("memberInput").value;
    console.log(memberName);
    window.location.href = "add_member/"+memberName;
}

