document.addEventListener("DOMContentLoaded", function () {
    const timerElement = document.getElementById("timer");
    const resendOtpBtn = document.getElementById("resendOtpBtn");
    let timeLeft = 60;

    const countdown = setInterval(() => {
      if (timeLeft <= 0) {
        clearInterval(countdown);
        resendOtpBtn.hidden = false;
        timerElement.innerHTML = "";
      } else {
        timerElement.innerHTML = `You can resend OTP in ${timeLeft} seconds.`;
      }
      timeLeft -= 1;
    }, 1000);

    resendOtpBtn.addEventListener("click", function () {
      timeLeft = 60;
      resendOtpBtn.hidden = true;
      countdown = setInterval(() => {
        if (timeLeft <= 0) {
          clearInterval(countdown);
          resendOtpBtn.hidden = false;
          timerElement.innerHTML = "";
        } else {
          timerElement.innerHTML = `You can resend OTP in ${timeLeft} seconds.`;
        }
        timeLeft -= 1;
      }, 1000);
    });
  });