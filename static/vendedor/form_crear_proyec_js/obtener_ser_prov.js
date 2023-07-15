const proveedorSelect = document.getElementById('proveedor_select');
const proveedorId = document.getElementById('proveedor_id');
const tipoServicioSelect = document.getElementsByName('tipo_servicio')[0];
const serviciosDisponibles = JSON.parse('{{ servicios_disponibles|safe }}');

proveedorSelect.addEventListener('change', () => {
    const proveedor = proveedorSelect.options[proveedorSelect.selectedIndex].dataset.proveedor;
    proveedorId.value = proveedor;

    tipoServicioSelect.innerHTML = '';
    serviciosDisponibles.filter(servicio => servicio.user_id == proveedor).forEach(servicio => {
      const option = document.createElement('option');
      option.value = servicio.id;
      option.text = servicio.nombre_servicio;
      tipoServicioSelect.add(option);
    });
});
