document.addEventListener("DOMContentLoaded", function() {
    const prevButton = document.querySelector(".carousel-button.prev");
    const nextButton = document.querySelector(".carousel-button.next");
    const carouselSteps = Array.from(document.querySelectorAll(".carousel-step"));
    let currentIndex = 0;
  
    // Mostrar el paso actual
    function showCurrentStep() {
      carouselSteps.forEach(function(step, index) {
        if (index === currentIndex) {
          step.classList.add("active");
        } else {
          step.classList.remove("active");
        }
      });
    }
  
    // Retroceder al paso anterior
    function prevStep() {
      if (currentIndex > 0) {
        currentIndex--;
        showCurrentStep();
        scrollToCurrentStep();
      }
    }
  
    // Avanzar al siguiente paso
    function nextStep() {
      if (currentIndex < carouselSteps.length - 1) {
        currentIndex++;
        showCurrentStep();
        scrollToCurrentStep();
      }
    }
  
    // Desplazarse al paso actual
    function scrollToCurrentStep() {
      const container = document.querySelector(".carousel-container");
      const currentStep = carouselSteps[currentIndex];
      container.scrollTo({
        left: currentStep.offsetLeft - container.offsetLeft,
        behavior: "smooth"
      });
    }
  
    // Asignar eventos a los botones de navegación
    prevButton.addEventListener("click", prevStep);
    nextButton.addEventListener("click", nextStep);
  });
  