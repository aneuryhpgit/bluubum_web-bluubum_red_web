var select = document.getElementById("proveedor_select");
var proveedorIdInput = document.getElementById("proveedor_id");

select.addEventListener("change", function() {
    var option = select.options[select.selectedIndex];
    var proveedorId = option.getAttribute("data-proveedor");
    proveedorIdInput.value = proveedorId;
});