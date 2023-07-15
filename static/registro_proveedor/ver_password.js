const passwordInput = document.getElementById("password");
const showPasswordButton = document.getElementById("show-password-btn");
const passwordInput2 = document.getElementById("password2");
const showPasswordButton2 = document.getElementById("show-password-btn2");

showPasswordButton.addEventListener("click", function() {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    showPasswordButton.innerHTML = '<i class="fa fa-eye-slash"></i>';
  } else {
    passwordInput.type = "password";
    showPasswordButton.innerHTML = '<i class="fa fa-eye"></i>';
  }
});


showPasswordButton2.addEventListener("click", function() {
  if (passwordInput2.type === "password") {
    passwordInput2.type = "text";
    showPasswordButton2.innerHTML = '<i class="fa fa-eye-slash"></i>';
  } else {
    passwordInput2.type = "password";
    showPasswordButton2.innerHTML = '<i class="fa fa-eye"></i>';
  }
});