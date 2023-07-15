const carousel = document.querySelector('.carousel_detail');
const carouselImages = carousel.querySelectorAll('img');
const prevButton = document.querySelector('.carousel-prev_detail');
const nextButton = document.querySelector('.carousel-next_detail');
let currentImageIndex = 0;

function showCurrentImage() {
  for (let i = 0; i < carouselImages.length; i++) {
    if (i === currentImageIndex) {
      carouselImages[i].style.display = 'block';
    } else {
      carouselImages[i].style.display = 'none';
    }
  }
}

prevButton.addEventListener('click', () => {
  currentImageIndex--;
  if (currentImageIndex < 0) {
    currentImageIndex = carouselImages.length - 1;
  }
  showCurrentImage();
});

nextButton.addEventListener('click', () => {
  currentImageIndex++;
  if (currentImageIndex > carouselImages.length - 1) {
    currentImageIndex = 0;
  }
  showCurrentImage();
});

showCurrentImage();