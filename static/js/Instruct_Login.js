
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.formulario');
    const nombreInput = form.querySelector('input[name="Nombre"]');
    const apellidosInput = form.querySelector('input[name="Apellido_P"]');
    const usuarioInput = form.querySelector('input[name="Usuario"]');
    const contrasenaInput = form.querySelector('input[name="Contrasena"]');
    const confirmCInput = form.querySelector('input[name="ConfirmarC"]');
    const direccionInput = form.querySelector('input[name="Direccion"]');

    const spanTextNombre = form.querySelector('.span_nombre'); 
    const spanTextApellidos = form.querySelector('.span_apellidos'); 
    const spanTextUsuario = form.querySelector('.span_usuario'); 
    const spanTextContrasena = form.querySelector('.span_contrasena'); 
    const spanTextConfirmC = form.querySelector('.span_confirmC'); 
    const spanTextDireccion = form.querySelector('.span_direccion');  

    const nombreRegex = /^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)?$/;
    const apellidosRegex = /^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)?$/;
    const usuarioRegex = /^[a-zA-Z0-9_-]{3,30}$/;
    const contrasenaRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=<>?]).{8,50}$/;
    const confirmCRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=<>?]).{8,50}$/;
    const direccionRegex = /^[^\s][\dA-Za-záéíóúÁÉÍÓÚÑñ\s\-#.,]+(,?\s?[\dA-Za-záéíóúÁÉÍÓÚÑñ\s\-#.,]+)*$/;

    form.addEventListener('submit', function(event) {
        const nombreValue = nombreInput.value;
        const apellidosValue = apellidosInput.value;
        const usuarioValue = usuarioInput.value;
        const contrasenaValue = contrasenaInput.value;
        const confirmCValue = confirmCInput.value;
        const direccionValue = direccionInput.value;

        let isValid = true;

        if (!nombreRegex.test(nombreValue)) {
            event.preventDefault();
            spanTextNombre.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextNombre.style.display = 'inline';
            nombreInput.style.borderBottom = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextNombre.style.display = 'none';
            nombreInput.style.borderBottom = '';
        }

        if (!apellidosRegex.test(apellidosValue)) {
            event.preventDefault();
            spanTextApellidos.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextApellidos.style.display = 'inline';
            apellidosInput.style.borderBottom = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextApellidos.style.display = 'none';
            apellidosInput.style.borderBottom = '';
        }

        if (!usuarioRegex.test(usuarioValue)) {
            event.preventDefault();
            spanTextUsuario.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextUsuario.style.display = 'inline';
            usuarioInput.style.borderBottom = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextUsuario.style.display = 'none';
            usuarioInput.style.borderBottom = '';
        }

        if (!contrasenaRegex.test(contrasenaValue)) {
            event.preventDefault();
            spanTextContrasena.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextContrasena.style.display = 'inline';
            contrasenaInput.style.borderBottom = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextContrasena.style.display = 'none';
            contrasenaInput.style.borderBottom = '';
        }

        if (!confirmCRegex.test(confirmCValue)) {
            event.preventDefault();
            spanTextConfirmC.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextConfirmC.style.display = 'inline';
            confirmCInput.style.borderBottom = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextConfirmC.style.display = 'none';
            confirmCInput.style.borderBottom = '';
        }

        if (!direccionRegex.test(direccionValue)) {
            event.preventDefault();
            spanTextDireccion.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextDireccion.style.display = 'inline';
            direccionInput.style.borderBottom = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextDireccion.style.display = 'none';
            direccionInput.style.borderBottom = '';
        }

        if (isValid) {
        }
    });
});



document.querySelectorAll('[id^="btn_actualizar"]').forEach(button => {
    button.addEventListener("click", function(event) {
        const modalId = this.getAttribute("data-bs-target");
        const form = document.querySelector(`${modalId} .upSub`);

        // Expresiones regulares para validación
        const nombreRegex = /^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)?$/;
        const apellidosRegex = /^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)?$/;
        const usuarioRegex = /^[a-zA-Z0-9_-]{3,30}$/;
        const direccionRegex = /^[^\s][\dA-Za-záéíóúÁÉÍÓÚÑñ\s\-#.,]+(,?\s?[\dA-Za-záéíóúÁÉÍÓÚÑñ\s\-#.,]+)*$/;

        const inputs = form.querySelectorAll('input');
        const spans = form.querySelectorAll('.span_text, .span_codigo, .span_precio, .span_PrecioAnt, .span_marca, .span_medida, .span_color, .span_material, .span_contenido, .span_acabado, .span_calidad');

        form.addEventListener('submit', function(event) {
            let isValid = true; // Variable para controlar si todo es válido

            inputs.forEach(input => {
                const name = input.name;
                const value = input.value;
                let regex = null;
                let span = null;

                // Selecciona el regex y el span correspondiente para cada campo
                switch (name) {
                    case 'Nombre_act':
                        regex = nombreRegex;
                        span = form.querySelector('.span_nombre');
                        break;
                    case 'Apellidos_act':
                        regex = apellidosRegex;
                        span = form.querySelector('.span_apellidos');
                        break;
                    case 'Usuario_act':
                        regex = usuarioRegex;
                        span = form.querySelector('.span_usuario');
                        break;
                    case 'Direccion_act':
                        regex = direccionRegex;
                        span = form.querySelector('.span_direccion');
                        break;
                }

                // Validación
                if (regex && !regex.test(value)) {
                    event.preventDefault(); // Prevenir envío

                    // Mostrar mensaje de error y cambiar borde
                    span.style.color = 'rgba(224, 16, 16, 0.952)';
                    span.style.display = 'block';
                    input.style.border = '2px solid rgba(224, 16, 16, 0.952)';
                    isValid = false;
                } else {
                    // Ocultar mensaje y resetear borde
                    span.style.display = 'none';
                    input.style.border = '';
                }
            });

            // Si es válido, puedes continuar con el envío del formulario
            if (isValid) {
                // Manejo adicional si se necesita
            }
        });
    });
});