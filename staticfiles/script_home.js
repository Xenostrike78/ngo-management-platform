document.addEventListener('DOMContentLoaded', function () {
    const swiper = new Swiper(".swiper-container", {
      loop: true,
      grabCursor: true,
      spaceBetween: 30,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
        dynamicBullets: true
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      breakpoints: {
        0: {
          slidesPerView: 1
        },
        620: {
          slidesPerView: 2
        },
        1024: {
          slidesPerView: 3
        }
      }
    });
  });

  function updateImageSrc() {
    const img = document.querySelector('.responsive-img');
    const isMobile = window.matchMedia("(max-width: 768px)").matches;
    const newSrc = isMobile ? img.getAttribute('data-src-small') : img.getAttribute('data-src-large');
    img.setAttribute('src', newSrc);
  }

  // Initial check
  updateImageSrc();

  // Update on window resize
  window.addEventListener('resize', updateImageSrc);