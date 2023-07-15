var progressCircle = document.getElementById('progress-circle');
var animacionEnCurso = false;

// Función para iniciar la animación del círculo de progreso
function iniciarAnimacion() {
  if (!animacionEnCurso) {
    progressCircle.style.display = 'block';
    progressCircle.classList.add('loader');
    animacionEnCurso = true;
  }
}

// Función para detener la animación del círculo de progreso
function detenerAnimacion() {
  progressCircle.classList.remove('loader');
  progressCircle.style.display = 'none';
  animacionEnCurso = false;
}

document.getElementById('save-button').addEventListener('click', function() {
  // Mostrar el círculo de progreso al hacer clic en el botón de guardar cambios
  iniciarAnimacion();

  // Simular el proceso de guardado
  setTimeout(function() {
    // Ocultar el círculo de progreso una vez completado el proceso de guardado
    detenerAnimacion();
  }, 200000); // Cambia 3000 por el tiempo real que tome el proceso de guardado
});

// Verificar si el usuario está en la vista donde se debe mantener girando el círculo de progreso
if (document.getElementById('progress-circle').style.display === 'block') {
  iniciarAnimacion();
}
