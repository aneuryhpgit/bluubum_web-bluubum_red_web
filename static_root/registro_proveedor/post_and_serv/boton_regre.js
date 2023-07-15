const btnRegresa = document.querySelector('.botn_detalle_regres');
    btnRegresa.addEventListener('click', function(event) {
    event.preventDefault();
    history.back();
});
