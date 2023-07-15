var modal = document.getElementById('modal_eliminar');
var btnEliminar = document.getElementById('modal-BTNeliminarServicio');

var abrirModal = document.querySelectorAll('.modal-btn');

for (var i = 0; i < abrirModal.length; i++) {
  abrirModal[i].addEventListener('click', function() {
    modal.style.display = 'block';
    btnEliminar.href = this.getAttribute('data-product-delete');
  });
}


function closeModal() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
}