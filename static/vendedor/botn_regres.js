const btnRegresar = document.querySelector('.btn_regresar');
btnRegresar.addEventListener('click', function(e) {
  e.preventDefault();
  window.history.back();
});