function addMember() {
  // Get the value of the input field
  var memberName = document.getElementById("memberInput").value;
  
  // Create an AJAX request to send the member name to the view
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // Handle the response from the server
      console.log(this.responseText);
    }
  };
  xhttp.open("POST", "{% url 'add_member' %}", true);  // Replace 'add_member' with the name of your view
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("member_name=" + memberName);
}

