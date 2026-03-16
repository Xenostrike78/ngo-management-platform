function toggleInput() {
  var toggleSwitch = document.getElementById("toggleSwitch");
  var emailInput = document.getElementById("emailInput");
  var phoneInput = document.getElementById("phoneInput");

  if (toggleSwitch.checked) {
    emailInput.style.display = "none";
    phoneInput.style.display = "block";
  } else {
    emailInput.style.display = "block";
    phoneInput.style.display = "none";
  }
}
