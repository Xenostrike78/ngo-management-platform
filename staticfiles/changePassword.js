// Passward check Code
function validatePasswords(event) {
    const password = document.getElementById('Password1').value;
    const confirmPassword = document.getElementById('Password2').value;
    if (password !== confirmPassword) {
      event.preventDefault();
      alert('Passwords do not match. Please try again.');
    }
  }

  // EYE Button function for Create Password
const togglePassword1 = document.getElementById("togglePassword1");
const passwordInput1 = document.getElementById("Password1");  // Input box ki id

togglePassword1.addEventListener("click", function (e) {
  // toggle the type attribute
  const type =
    passwordInput1.getAttribute("type") === "password" ? "text" : "password";
  passwordInput1.setAttribute("type", type);
  // toggle the eye icon
  this.classList.toggle("fa-eye-slash");
});

// EYE Button function for Confirm Password
const togglePassword2 = document.getElementById("togglePassword2");
const passwordInput2 = document.getElementById("Password2");  // Input box ki id

togglePassword2.addEventListener("click", function (e) {
  // toggle the type attribute
  const type =
    passwordInput2.getAttribute("type") === "password" ? "text" : "password";
  passwordInput2.setAttribute("type", type);
  // toggle the eye icon
  this.classList.toggle("fa-eye-slash");
});