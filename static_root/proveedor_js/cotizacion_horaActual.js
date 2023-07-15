function obtenerFechaHoraActual() {
    const ahora = new Date();
    const dia = ahora.getDate();
    const mes = ahora.getMonth() + 1; // Los meses en JavaScript van de 0 a 11
    const anio = ahora.getFullYear();
    const hora = ahora.getHours();
    const minutos = ahora.getMinutes();
    const segundos = ahora.getSeconds();
    return anio + "-" + mes + "-" + dia + " " + hora + ":" + minutos + ":" + segundos;
  }

  const inputFechaHoraActual = document.getElementById("fecha-hora-actual");
  inputFechaHoraActual.value = obtenerFechaHoraActual();