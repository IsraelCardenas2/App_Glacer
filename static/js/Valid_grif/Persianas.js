
//----------------------------------------- Expreciones regulares Add Pisos y Muros ------------------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.form_reg');
    const nombreInput = form.querySelector('input[name="Nombre"]');
    const codigoInput = form.querySelector('input[name="Codigo"]');
    const precioInput = form.querySelector('input[name="Precio"]');
    const precioantInput = form.querySelector('input[name="PrecioAnt"]');
    const marcaInput = form.querySelector('input[name="Marca"]');
    const colorInput = form.querySelector('input[name="Color"]');
    const materialInput = form.querySelector('input[name="Material"]');
    const complementoInput = form.querySelector('input[name="Complementos"]');
    const tiempo_entregaInput = form.querySelector('input[name="Tiempo_entrega"]');

    const spanTextNombre = form.querySelector('.span_text'); // Mensaje de error para Nombre
    const spanTextcodigo = form.querySelector('.span_codigo'); // Mensaje de error para el campo Codigo
    const spanTextprecio = form.querySelector('.span_precio'); // Mensaje de error para Precio
    const spanTextprecioant = form.querySelector('.span_PrecioAnt'); // Mensaje de error para Precio
    const spanTextmarca = form.querySelector('.span_marca'); // Mensaje de error para el campo Marca
    const spanTextcolor = form.querySelector('.span_color'); // Mensaje de error para campo color
    const spanTextmaterial = form.querySelector('.span_material'); // Mensaje de error para el campo Material
    const spanTextcomplemento = form.querySelector('.span_complementos'); // Mensaje de error para campo Acabado
    const spanTexttiempo_entrega = form.querySelector('.span_tiempo_entrega'); // Mensaje de error para campo Acabado

    const nombreRegex = /^[A-Z][a-z]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+)+$/;
    const precioRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/; // Solo números y opcionalmente un decimal
    const precioantRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/; // Solo números y opcionalmente un decimal
    const materialRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
    const marcaRegex = /^(?! )(?:[A-Z][a-záéíóúñÑ]+)(?: (?:[A-Z][a-záéíóúñÑ]+))?(?<! )$/;
    const codigoRegex = /^[A-Za-z0-9-]{1,15}$/;
    const colorRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z][a-záéíóúÁÉÍÓÚñÑ]+){0,2}$/;
    const complementoRegex = /^[A-Z0-9][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z0-9a-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
    const tiempo_entregaRegex = /^[A-Z0-9][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z0-9a-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;

    form.addEventListener('submit', function(event) {
        const nombreValue = nombreInput.value;
        const precioValue = precioInput.value;
        const precioantValue = precioantInput.value;
        const materialValue = materialInput.value;
        const marcaValue = marcaInput.value;
        const codigoValue = codigoInput.value;
        const colorValue = colorInput.value;
        const complementoValue = complementoInput.value;
        const tiempo_entregaValue = tiempo_entregaInput.value;

        let isValid = true; // Variable para controlar si todo es válido

        // Validar Nombre
        if (!nombreRegex.test(nombreValue)) {
            event.preventDefault();
            spanTextNombre.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextNombre.style.display = 'inline';
            nombreInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextNombre.style.display = 'none';
            nombreInput.style.border = '';
        }

        // Validar Precio
        if (!precioRegex.test(precioValue) || precioValue === '') {
            event.preventDefault();
            spanTextprecio.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextprecio.style.display = 'inline';
            precioInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextprecio.style.display = 'none';
            precioInput.style.border = '';
        }
        // Validar Precio Anterior
        if (!precioantRegex.test(precioantValue) || precioantValue === '') {
            event.preventDefault(); 
            spanTextprecioant.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextprecioant.style.display = 'inline';
            precioantInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
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
            spanTextmaterial.style.display = 'none';
            materialInput.style.border = '';
        }
        // Validar Complementos
        if (!complementoRegex.test(complementoValue) || complementoValue === '') {
            event.preventDefault();
            spanTextcomplemento.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextcomplemento.style.display = 'inline';
            complementoInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextcomplemento.style.display = 'none';
            complementoInput.style.border = '';
        }
        // Validar Tiempo de entrega
        if (!tiempo_entregaRegex.test(tiempo_entregaValue) || tiempo_entregaValue === '') {
            event.preventDefault();
            spanTexttiempo_entrega.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTexttiempo_entrega.style.display = 'inline';
            tiempo_entregaInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTexttiempo_entrega.style.display = 'none';
            tiempo_entregaInput.style.border = '';
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
            // Ocultar mensaje y resetear borde
            spanTextmarca.style.display = 'none';
            marcaInput.style.border = '';
        }

        // Validar Codigo
        if (!codigoRegex.test(codigoValue) || codigoValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextcodigo.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextcodigo.style.display = 'inline';
            codigoInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextcodigo.style.display = 'none';
            codigoInput.style.border = '';
        }

        // Validar Color
        if (!colorRegex.test(colorValue) || colorValue === '') {
            event.preventDefault(); // Prevenir envío

            // Mostrar mensaje y cambiar borde
            spanTextcolor.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextcolor.style.display = 'inline';
            colorInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextcolor.style.display = 'none';
            colorInput.style.border = '';
        }

        // Si ambos son válidos, se enviará el formulario
        if (isValid) {
            // Aquí puedes manejar el envío del formulario si es necesario
        }
    });
});


// ---------------------------------------- Secciòn de actualizaciòn --------------------------------


//----------------------------------------- Expreciones regulares Add Pisos y Muros ------------------------------------------------------------------------------------------------------------

document.querySelectorAll('[id^="btn_actualizar"]').forEach(button => {
    button.addEventListener("click", function(event) {
        const modalId = this.getAttribute("data-bs-target");
        const form = document.querySelector(`${modalId} .upPersiana`);

        // Expresiones regulares para validación
        const nombreRegex = /^[A-Z][a-z]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+)+$/;
        const precioRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/;
        const precioantRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/;
        const materialRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
        const marcaRegex = /^(?! )(?:[A-Z][a-záéíóúñÑ]+)(?: (?:[A-Z][a-záéíóúñÑ]+))?(?<! )$/;
        const codigoRegex = /^[A-Za-z0-9-]{1,15}$/;
        const colorRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z][a-záéíóúÁÉÍÓÚñÑ]+){0,2}$/;
        const complementoRegex = /^[A-Z0-9][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z0-9a-záéíóúÁÉÍÓÚñÑ]+){0,59}$/;
        const tiempo_entregaRegex = /^[A-Z0-9][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z0-9a-záéíóúÁÉÍÓÚñÑ]+){0,59}$/;

        const inputs = form.querySelectorAll('input');
        const spans = form.querySelectorAll('.span_text, .span_codigo, .span_precio, .span_PrecioAnt, .span_marca, .span_color, .span_material, .span_complementos, .span_tiempo_entrega');

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
                    case 'Color_act':
                        regex = colorRegex;
                        span = form.querySelector('.span_color');
                        break;
                    case 'Material_act':
                        regex = materialRegex;
                        span = form.querySelector('.span_material');
                        break;
                    case 'Complementos_act':
                        regex = complementoRegex;
                        span = form.querySelector('.span_complementos');
                        break;
                    case 'Tiempo_entrega_act':
                        regex = tiempo_entregaRegex;
                        span = form.querySelector('.span_tiempo_entrega');
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
