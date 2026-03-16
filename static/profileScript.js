document
  .getElementById("edit-profile-picture-button")
  .addEventListener("click", function () {
    document.getElementById("profile-picture").click();
  });

document
  .getElementById("profile-picture")
  .addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        const img = document.getElementById("profile-picture-preview");
        img.src = e.target.result;
        img.style.display = "block";
      };
      reader.readAsDataURL(file);
    }
  });

document
  .getElementById("edit-profile-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData();
    const fileInput = document.getElementById("profile-picture");
    const emailInput = document.getElementById("email").value;

    if (fileInput.files[0]) {
      formData.append("profile-picture", fileInput.files[0]);
    }
    formData.append("email", emailInput);

    fetch("/api/update-profile", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          alert("Profile updated successfully!");
        } else {
          alert("Error updating profile.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred.");
      });
  });
