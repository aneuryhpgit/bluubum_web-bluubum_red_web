document.addEventListener('DOMContentLoaded', function() {

  document.getElementById("btn-show").addEventListener("click", function(){
    var div = document.getElementById("caj-alert-show");
    if (div.style.display === "") {
      div.style.display = "none";
    } else {
      div.style.display = "block";
    }
  });

});

  
  
  
  
  