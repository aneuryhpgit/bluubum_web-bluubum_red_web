const usuarioInput = document.getElementById('usuario');
const usuarioSugeridoDiv = document.getElementById('usuario-sugerido');

// Agrega un event listener al input de usuario para que cada vez que se escriba algo, se compruebe si ya existe
usuarioInput.addEventListener('input', function() {
    const usuario = usuarioInput.value;
    // Envía una petición AJAX al servidor para verificar si el usuario ya existe
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            // Si el usuario ya existe, crea un input select con las opciones sugeridas
            if (xhr.status === 200) {
                const usuariosSugeridos = JSON.parse(xhr.responseText);
                if (usuariosSugeridos.length > 0) {
                    let opciones = '';
                    for (const usuarioSugerido of usuariosSugeridos) {
                        opciones += `<option value="${usuarioSugerido}">${usuarioSugerido}</option>`;
                    }
                    usuarioSugeridoDiv.innerHTML = `<label for="usuario-sugerido">Seleccione uno de los siguientes:</label>
                                                    <select id="usuario-sugerido" name="usuario-sugerido">
                                                        ${opciones}
                                                    </select>`;
                } else {
                    usuarioSugeridoDiv.innerHTML = '';
                }
            }
        }
    };
    xhr.open('GET', `/registro_proveedor?usuario=${usuario}`);
    xhr.send();
});
