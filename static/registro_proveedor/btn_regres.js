const btnRegresar = document.querySelector('.btn_regresar');
    btnRegresar.addEventListener('click', function(event) {
    event.preventDefault();
    history.back();
});
