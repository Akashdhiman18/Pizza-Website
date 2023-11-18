let navbar = document.querySelector('.header .flex .navbar');


let popupform=document.getElement('myForm')
function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}
function showSuccessMessage() {
  var successMessage = document.getElementById("successMessage");

  // Display the success message
  successMessage.style.display = "block";

  // Optionally, you can hide the form after displaying the success message
  var form = document.getElementById("myForm");
  form.style.display = "none";
}
function showLoadingSpinner() {
  document.getElementById("loginBtn").style.display = "none";
  document.getElementById("loadingSpinner").style.display = "inline-block";
}