// Función para mostrar la imagen previa
function previewImage(input, imgPreview) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function(e) {
      imgPreview.src = e.target.result;
    }
    reader.readAsDataURL(input.files[0]); // Lee el archivo y lo convierte en una URL
  }
}

// Evento para cambiar la imagen previa cuando se selecciona un archivo
window.onload = function() {
  var fileInputs = document.querySelectorAll('.subirImg');
  
  fileInputs.forEach(function(fileInput) {
    var imgPreview = fileInput.parentElement.querySelector('img');
    
    fileInput.addEventListener('change', function() {
      previewImage(this, imgPreview);
    });
  });
};



