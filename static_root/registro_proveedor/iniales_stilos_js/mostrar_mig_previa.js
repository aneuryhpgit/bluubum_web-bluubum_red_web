function previewImage(input) {
  var preview = document.getElementById('img-preview');
  var file    = input.files[0];
  var reader  = new FileReader();

  reader.onloadend = function () {
    preview.src = reader.result;
  }

  if (file) {
    reader.readAsDataURL(file);
  } else {
    preview.src = "";
  }
}

var fileInput = document.getElementById('file');
fileInput.addEventListener('change', function() {
  previewImage(this);
});
  