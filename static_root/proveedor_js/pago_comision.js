// Obtener los elementos del DOM
var fechaInicio = document.getElementById("fecha_nicio");
var fechaPagoComision = document.getElementById("fecha_pago_comision");

// Agregar un event listener para detectar cambios en la fecha de inicio
fechaInicio.addEventListener("change", function() {
  // Obtener la fecha de inicio en formato ISO y convertirla a objeto Date
  var fechaInicioValue = fechaInicio.value;
  var fechaInicioObj = new Date(fechaInicioValue);

  // Sumar 15 días a la fecha de inicio
  var fechaPagoComisionObj = new Date(fechaInicioObj.getTime() + (10 * 24 * 60 * 60 * 1000));

  // Formatear la fecha de pago de la comisión en formato "YYYY-MM-DD"
  var fechaPagoComisionValue = fechaPagoComisionObj.toISOString().substring(0, 10);

  // Guardar la fecha de pago de la comisión en el input correspondiente
  fechaPagoComision.value = fechaPagoComisionValue;
});
