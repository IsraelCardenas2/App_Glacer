document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('my-button');
    const icon = document.getElementById('toggle-icon');

    icon.addEventListener('click', function() {
        if (button.classList.contains('hidden')) {
            button.classList.remove('hidden'); // Muestra el botón
        } else {
            button.classList.add('hidden'); // Oculta el botón
        }
    });
});
// -------------------------- Este apartado es para saber Si es Sub o Admin y ejecutar la función de eliminar -----------
function confirmDelete(url, privilegio, notificarRuta) {
    if (privilegio === "Subadministrador") {
        Swal.fire({
            title: 'Sin permisos',
            text: 'No tienes permisos para eliminar productos.',
            icon: 'warning',
            showCancelButton: true,
            cancelButtonText: 'Cerrar',
            confirmButtonText: 'Notificar',
            customClass: {
                cancelButton: 'btn btn-secondary',
                confirmButton: 'btn btn-primary'
            }
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = notificarRuta;
            }
        });
    } else if (privilegio === "Administrador") {
        Swal.fire({
            title: '¿Estás seguro de eliminar el producto?',
            icon: 'error',
            showCancelButton: true,
            cancelButtonText: 'Cancelar',
            confirmButtonText: 'Confirmar',
            customClass: {
                cancelButton: 'btn btn-secondary',
                confirmButton: 'btn btn-danger'
            }
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = url;
            }
        });
    }
}