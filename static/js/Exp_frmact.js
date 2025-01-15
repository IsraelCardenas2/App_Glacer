//----------------------------------------- Expreciones regulares Add Pisos y Muros ------------------------------------------------------------------------------------------------------------

document.querySelectorAll('[id^="btn_actualizar"]').forEach(button => {
    button.addEventListener("click", function(event) {
        const modalId = this.getAttribute("data-bs-target");
        const form = document.querySelector(`${modalId} .upPisMur`);

        // Expresiones regulares para validación
        const nombreRegex = /^(?! )[A-Z][a-záéíóúñ]+(?: [A-Z][a-záéíóúñ]+){1,2}(?<! )$/;
        const codigoRegex = /^[A-Za-z0-9-]{1,15}$/;
        const precioRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/;
        const precioantRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/;
        const medidaRegex = /^\d{1,4}(\.\d{1,4})?x\d{1,4}(\.\d{1,4})?$/;
        const colorRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z][a-záéíóúÁÉÍÓÚñÑ]+){0,2}$/;
        const marcaRegex = /^(?! )(?:[A-Z][a-záéíóúñ]+)(?: (?:[A-Z][a-záéíóú]+))?(?<! )$/;
        const materialRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
        const acabadoRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
        const contenidoRegex = /^[0-9]+(\.[0-9]{1,2})?$/;
        const calidadRegex = /^(?! )(?:[A-Z][a-z]+)(?: (?:[A-Z][a-z]+))?(?<! )$/;

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
                        span = form.querySelector('.span_text');
                        break;
                    case 'Codigo_act':
                        regex = codigoRegex;
                        span = form.querySelector('.span_codigo');
                        break;
                    case 'Precio_act':
                        regex = precioRegex;
                        span = form.querySelector('.span_precio');
                        break;
                    case 'PrecioAnt_act':
                        regex = precioantRegex;
                        span = form.querySelector('.span_PrecioAnt');
                        break;
                    case 'Marca_act':
                        regex = marcaRegex;
                        span = form.querySelector('.span_marca');
                        break;
                    case 'Medida_act':
                        regex = medidaRegex;
                        span = form.querySelector('.span_medida');
                        break;
                    case 'Color_act':
                        regex = colorRegex;
                        span = form.querySelector('.span_color');
                        break;
                    case 'Material_act':
                        regex = materialRegex;
                        span = form.querySelector('.span_material');
                        break;
                    case 'Acabado_act':
                        regex = acabadoRegex;
                        span = form.querySelector('.span_acabado');
                        break;
                    case 'Contenido_act':
                        regex = contenidoRegex;
                        span = form.querySelector('.span_contenido');
                        break;
                    case 'Calidad_act':
                        regex = calidadRegex;
                        span = form.querySelector('.span_calidad');
                        break;
                }

                // Validación
                if (regex && !regex.test(value)) {
                    event.preventDefault(); // Prevenir envío

                    // Mostrar mensaje de error y cambiar borde
                    span.style.color = 'rgba(224, 16, 16, 0.952)';
                    span.style.display = 'inline';
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
