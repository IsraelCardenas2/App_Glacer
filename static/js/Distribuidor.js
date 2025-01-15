document.addEventListener("DOMContentLoaded", function () {
    var header = document.getElementById("header");

    if (header) {
        // Inicializamos Headroom.js solo si el encabezado existe
        var headroom = new Headroom(header);
        console.log('Headroom.js ha sido inicializado');
        headroom.init();  // Inicializamos Headroom.js
    }
});

let lastScrollTop = 0;
const header = document.getElementById('header');

window.addEventListener('scroll', function() {
let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

if (currentScroll > lastScrollTop && currentScroll > 100) {
// Si el usuario hace scroll hacia abajo y ha desplazado más de 100px
header.style.transform = "translateY(-100%)"; // Ocultamos el encabezado
} else if (currentScroll < lastScrollTop) {
// Si el usuario hace scroll hacia arriba
header.style.transform = "translateY(0)"; // Mostramos el encabezado
}
lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // Evita que lastScrollTop sea negativo
});
//----------------------------------------- Exn_negociones regulares Add Pisos y Muros ------------------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.form_reg');
    const nombreInput = form.querySelector('input[name="Nombre"]');
    const puestoInput = form.querySelector('input[name="Puesto"]');
    const n_negocioInput = form.querySelector('input[name="N_negocio"]');
    const giroInput = form.querySelector('input[name="Giro"]');
    const ubicacionInput = form.querySelector('input[name="Ubicacion"]');
    const correoInput = form.querySelector('input[name="Correo"]');
    const telefonoInput = form.querySelector('input[name="Telefono"]');
    const experienciaInput = form.querySelector('input[name="Experiencia"]');

    const spanTextNombre = form.querySelector('.span_nombre'); // Mensaje de error para Nombre
    const spanTextpuesto = form.querySelector('.span_puesto'); // Mensaje de error para el campo Puesto
    const spanTextn_negocio = form.querySelector('.span_n_negocio'); // Mensaje de error para N_negocio
    const spanTextgiro = form.querySelector('.span_giro'); // Mensaje de error para N_negocio
    const spanTextubicacion = form.querySelector('.span_ubicacion'); // Mensaje de error para el campo Ubicacion
    const spanTextcorreo = form.querySelector('.span_correo'); // Mensaje de error para campo correo
    const spanTexttelefono = form.querySelector('.span_telefono'); // Mensaje de error para el campo Telefono
    const spanTextexperiencia = form.querySelector('.span_experiencia'); // Mensaje de error para campo Acabado

    const nombreRegex = /^[A-Z][a-z]+( [a-zA-ZáéíóúÁÉÍÓÚ]+)+(\s+[a-zA-ZáéíóúÁÉÍÓÚ]+)+$/;
    const n_negocioRegex = /^[A-Z][a-zA-Z]*( [a-zA-ZáéíóúÁÉÍÓÚ]+)+(\s+[a-zA-ZáéíóúÁÉÍÓÚ]+)*$/; // Solo Econo Pisos Institucionales, Elegant Recubrimientos, Interceramic la ezquinita pivil
    const giroRegex = /^[A-Z][a-zA-Z\s]+$/; // Solo Energía, Construcción e inmobiliaria, Tecnología y software
    const telefonoRegex = /^\(?\d{2,4}\)?[\s\-]?\d{2,4}[\s\-]?\d{2,4}$/; // 123 456 7890 (123)-456-7890
    const experienciaRegex = /^[A-Z][a-z]+(?:[,.]?[ ]?[a-z]+)+$/; // Texto de prueba, con una coma. Hola mundo
    const ubicacionRegex = /^[^\s][\dA-Za-záéíóúÁÉÍÓÚÑñ\s\-#.,]+(,?\s?[\dA-Za-záéíóúÁÉÍÓÚÑñ\s\-#.,]+)*$/;
    const puestoRegex = /^[A-Z][a-zA-Z\s]+$/;  // Administrador de sistemas, Gerente de ventas
    const correoRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/; //usuario@example.com, first_last123@subdomain.example.org, user.name@domain.co

    form.addEventListener('submit', function(event) {
        const nombreValue = nombreInput.value;
        const n_negocioValue = n_negocioInput.value;
        const giroValue = giroInput.value;
        const telefonoValue = telefonoInput.value;
        const experienciaValue = experienciaInput.value;
        const ubicacionValue = ubicacionInput.value;
        const puestoValue = puestoInput.value;
        const correoValue = correoInput.value;

        let isValid = true; // Variable para controlar si todo es válido

        // Validar Nombre
        if (!nombreRegex.test(nombreValue)) {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextNombre.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextNombre.style.display = 'inline';
            nombreInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextNombre.style.display = 'none';
            nombreInput.style.border = '';
        }

        // Validar N_negocio
        if (!n_negocioRegex.test(n_negocioValue) || n_negocioValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextn_negocio.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextn_negocio.style.display = 'inline';
            n_negocioInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextn_negocio.style.display = 'none';
            n_negocioInput.style.border = '';
        }
        // Validar N_negocio Anterior
        if (!giroRegex.test(giroValue) || giroValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextgiro.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextgiro.style.display = 'inline';
            giroInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextgiro.style.display = 'none';
            giroInput.style.border = '';
        } 
        // Validar telefono
        if (!telefonoRegex.test(telefonoValue) || telefonoValue === '') {
            event.preventDefault(); 

            spanTexttelefono.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTexttelefono.style.display = 'inline';
            telefonoInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTexttelefono.style.display = 'none';
            telefonoInput.style.border = '';
        }

        // Validar Experiencia
        if (!experienciaRegex.test(experienciaValue) || experienciaValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextexperiencia.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextexperiencia.style.display = 'inline';
            experienciaInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextexperiencia.style.display = 'none';
            experienciaInput.style.border = '';
        }


        // Validar ubicacion
        if (!ubicacionRegex.test(ubicacionValue) || ubicacionValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextubicacion.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextubicacion.style.display = 'inline';
            ubicacionInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextubicacion.style.display = 'none';
            ubicacionInput.style.border = '';
        }

        // Validar Puesto
        if (!puestoRegex.test(puestoValue) || puestoValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextpuesto.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextpuesto.style.display = 'inline';
            puestoInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextpuesto.style.display = 'none';
            puestoInput.style.border = '';
        }

        // Validar Correo
        if (!correoRegex.test(correoValue) || correoValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextcorreo.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextcorreo.style.display = 'inline';
            correoInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextcorreo.style.display = 'none';
            correoInput.style.border = '';
        }

        // Si ambos son válidos, se enviará el formulario
        if (isValid) {
            // Aquí puedes manejar el envío del formulario si es necesario
        }
    });
});


