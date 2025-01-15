
//----------------------------------------- Expreciones regulares Add Pisos y Muros ------------------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.form_reg');
    const nombreInput = form.querySelector('input[name="Nombre"]');
    const codigoInput = form.querySelector('input[name="Codigo"]');
    const precioInput = form.querySelector('input[name="Precio"]');
    const precioantInput = form.querySelector('input[name="PrecioAnt"]');
    const medidaInput = form.querySelector('input[name="Medida"]');
    const colorInput = form.querySelector('input[name="Color"]');
    const marcaInput = form.querySelector('input[name="Marca"]');
    const materialInput = form.querySelector('input[name="Material"]');
    const flujo_aguaInput = form.querySelector('input[name="Flujo_agua"]');
    const presionInput = form.querySelector('input[name="Presion"]');

    const spanTextNombre = form.querySelector('.span_text'); // Mensaje de error para Nombre
    const spanTextcodigo = form.querySelector('.span_codigo'); // Mensaje de error para el campo Codigo
    const spanTextprecio = form.querySelector('.span_precio'); // Mensaje de error para Precio
    const spanTextprecioant = form.querySelector('.span_PrecioAnt'); // Mensaje de error para Precio
    const spanTextmedida = form.querySelector('.span_medida'); // Mensaje de error para el campo Medida
    const spanTextcolor = form.querySelector('.span_color'); // Mensaje de error para campo color
    const spanTextmarca = form.querySelector('.span_marca'); // Mensaje de error para el campo Marca
    const spanTextmaterial = form.querySelector('.span_material'); // Mensaje de error para el campo Material
    const spanTextflujo_agua = form.querySelector('.span_flujo_agua'); // Mensaje de error para campo Flujo_agua
    const spanTextpresion = form.querySelector('.span_presion'); // Mensaje de error para campo presion

    const nombreRegex = /^[A-Z][a-z]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+)+$/;
    const codigoRegex = /^[A-Za-z0-9-]{1,15}$/;
    const precioRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/; // Solo números y opcionalmente un decimal
    const precioantRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/; // Solo números y opcionalmente un decimal
    const medidaRegex = /^\d{1,4}(\.\d{1,4})?x\d{1,4}(\.\d{1,4})?$/;
    const colorRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z][a-záéíóúÁÉÍÓÚñÑ]+){0,2}$/;
    const marcaRegex = /^(?! )(?:[A-Z][a-záéíóúñÑ]+)(?: (?:[A-Z][a-záéíóúñÑ]+))?(?<! )$/;
    const materialRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
    const flujo_aguaRegex = /^\d+(\.\d+)?\s+a\s+\d+(\.\d+)?$/;
    const presionRegex = /^[A-Z][a-z]+(\s[A-Z][a-z]+)?$/;

    form.addEventListener('submit', function(event) {
        const nombreValue = nombreInput.value;
        const codigoValue = codigoInput.value;
        const precioValue = precioInput.value;
        const precioantValue = precioantInput.value;
        const medidaValue = medidaInput.value;
        const colorValue = colorInput.value;
        const marcaValue = marcaInput.value;
        const materialValue = materialInput.value;
        const flujo_aguaValue = flujo_aguaInput.value;
        const presionValue = presionInput.value;

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

        // Validar Precio
        if (!precioRegex.test(precioValue) || precioValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextprecio.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextprecio.style.display = 'inline';
            precioInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextprecio.style.display = 'none';
            precioInput.style.border = '';
        }
        // Validar Precio Anterior
        if (!precioantRegex.test(precioantValue) || precioantValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextprecioant.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextprecioant.style.display = 'inline';
            precioantInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextprecioant.style.display = 'none';
            precioantInput.style.border = '';
        } 
        // Validar material
        if (!materialRegex.test(materialValue) || materialValue === '') {
            event.preventDefault(); 

            spanTextmaterial.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextmaterial.style.display = 'inline';
            materialInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextmaterial.style.display = 'none';
            materialInput.style.border = '';
        }

        // Validar Flujo de agua
        if (!flujo_aguaRegex.test(flujo_aguaValue) || flujo_aguaValue === '') {
            event.preventDefault();
            spanTextflujo_agua.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextflujo_agua.style.display = 'inline';
            flujo_aguaInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextflujo_agua.style.display = 'none';
            flujo_aguaInput.style.border = '';
        }
        // Validar Presion
        if (!presionRegex.test(presionValue) || presionValue === '') {
            event.preventDefault();
            spanTextpresion.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextpresion.style.display = 'inline';
            presionInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextpresion.style.display = 'none';
            presionInput.style.border = '';
        }

        // Validar marca
        if (!marcaRegex.test(marcaValue) || marcaValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextmarca.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextmarca.style.display = 'inline';
            marcaInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextmarca.style.display = 'none';
            marcaInput.style.border = '';
        }
        // Validar medida
        if (!medidaRegex.test(medidaValue) || medidaValue === '') {
            event.preventDefault();
            spanTextmedida.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextmedida.style.display = 'inline';
            medidaInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextmedida.style.display = 'none';
            medidaInput.style.border = '';
        }
        // Validar Codigo
        if (!codigoRegex.test(codigoValue) || codigoValue === '') {
            event.preventDefault();
            spanTextcodigo.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextcodigo.style.display = 'inline';
            codigoInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextcodigo.style.display = 'none';
            codigoInput.style.border = '';
        }

        // Validar Color
        if (!colorRegex.test(colorValue) || colorValue === '') {
            event.preventDefault();
            spanTextcolor.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextcolor.style.display = 'inline';
            colorInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextcolor.style.display = 'none';
            colorInput.style.border = '';
        }
        if (isValid) {
        }
    });
});


// ---------------------------------------- Secciòn de actualizaciòn --------------------------------


//----------------------------------------- Expreciones regulares Add Pisos y Muros ------------------------------------------------------------------------------------------------------------

document.querySelectorAll('[id^="btn_actualizar"]').forEach(button => {
    button.addEventListener("click", function(event) {
        const modalId = this.getAttribute("data-bs-target");
        const form = document.querySelector(`${modalId} .upBrazo`);

        // Expresiones regulares para validación
        const nombreRegex = /^[A-Z][a-z]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+)+$/;
        const codigoRegex = /^[A-Za-z0-9-]{1,15}$/;
        const precioRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/;
        const precioantRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/;
        const medidaRegex = /^\d{1,4}(\.\d{1,4})?x\d{1,4}(\.\d{1,4})?$/;
        const colorRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z][a-záéíóúÁÉÍÓÚñÑ]+){0,2}$/;
        const marcaRegex = /^(?! )(?:[A-Z][a-záéíóúñÑ]+)(?: (?:[A-Z][a-záéíóúñÑ]+))?(?<! )$/;
        const materialRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
        const flujo_aguaRegex = /^\d+(\.\d+)?\s+a\s+\d+(\.\d+)?$/;
        const presionRegex = /^[A-Z][a-z]+(\s[A-Z][a-z]+)?$/;

        const inputs = form.querySelectorAll('input');
        const spans = form.querySelectorAll('.span_text, .span_codigo, .span_precio, .span_PrecioAnt, .span_marca, .span_medida, .span_color, .span_material, .span_flujo_agua, .span_presion');

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
                    case 'Medida_act':
                        regex = medidaRegex;
                        span = form.querySelector('.span_medida');
                        break;
                    case 'Marca_act':
                        regex = marcaRegex;
                        span = form.querySelector('.span_marca');
                        break;
                    case 'Color_act':
                        regex = colorRegex;
                        span = form.querySelector('.span_color');
                        break;
                    case 'Material_act':
                        regex = materialRegex;
                        span = form.querySelector('.span_material');
                        break;
                    case 'Flujo_agua_act':
                        regex = flujo_aguaRegex;
                        span = form.querySelector('.span_flujo_agua');
                        break;
                    case 'Presion_act':
                        regex = presionRegex;
                        span = form.querySelector('.span_presion');
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
