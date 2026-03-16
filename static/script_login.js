const togglePassword = document.getElementById("togglePassword");
const passwordInput = document.getElementById("exampleInputPassword1");

togglePassword.addEventListener("click", function (e) {
  // toggle the type attribute
  const type =
    passwordInput.getAttribute("type") === "password" ? "text" : "password";
  passwordInput.setAttribute("type", type);
  // toggle the eye icon
  this.classList.toggle("fa-eye-slash");
});
