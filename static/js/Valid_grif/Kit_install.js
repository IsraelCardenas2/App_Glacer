
//----------------------------------------- Expreciones regulares Add Pisos y Muros ------------------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.form_reg');
    const nombreInput = form.querySelector('input[name="Nombre"]');
    const codigoInput = form.querySelector('input[name="Codigo"]');
    const precioInput = form.querySelector('input[name="Precio"]');
    const precioantInput = form.querySelector('input[name="PrecioAnt"]');
    const marcaInput = form.querySelector('input[name="Marca"]');
    const medida_llavesInput = form.querySelector('input[name="Medida_llaves"]');
    const materialInput = form.querySelector('input[name="Material"]');
    const contracanastaInput = form.querySelector('input[name="Contracanasta"]');
    const alimentadorInput = form.querySelector('input[name="Alimentador"]');
    const complementosInput = form.querySelector('input[name="Complementos"]');

    const spanTextNombre = form.querySelector('.span_text'); // Mensaje de error para Nombre
    const spanTextcodigo = form.querySelector('.span_codigo'); // Mensaje de error para el campo Codigo
    const spanTextprecio = form.querySelector('.span_precio'); // Mensaje de error para Precio
    const spanTextprecioant = form.querySelector('.span_PrecioAnt'); // Mensaje de error para Precio
    const spanTextmedida_llaves = form.querySelector('.span_medida_llaves'); // Mensaje de error para el campo medida_llaves
    const spanTextcontracanasta = form.querySelector('.span_contracanasta'); // Mensaje de error para campo color
    const spanTextmarca = form.querySelector('.span_marca'); // Mensaje de error para el campo Marca
    const spanTextmaterial = form.querySelector('.span_material'); // Mensaje de error para el campo Material
    const spanTextalimentador = form.querySelector('.span_alimentador'); // Mensaje de error para campo Flujo_agua
    const spanTextcomplementos = form.querySelector('.span_complementos'); // Mensaje de error para campo complementos

    const nombreRegex = /^[A-Z][a-z]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+)+$/;
    const codigoRegex = /^[A-Za-z0-9-]{1,15}$/;
    const precioRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/; // Solo números y opcionalmente un decimal
    const precioantRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/; // Solo números y opcionalmente un decimal
    const medida_llavesRegex = /^\d{1,4}(\.\d{1,4})?x\d{1,4}(\.\d{1,4})?$/;
    const contracanastaRegex = /^\d+$/;
    const marcaRegex = /^(?! )(?:[A-Z][a-záéíóúñÑ]+)(?: (?:[A-Z][a-záéíóúñÑ]+))?(?<! )$/;
    const materialRegex = /^[A-Z0-9][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z0-9a-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
    const alimentadorRegex = /^\d+$/;
    const complementosRegex = /^[A-Z0-9][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z0-9a-záéíóúÁÉÍÓÚñÑ]+){0,59}$/;

    form.addEventListener('submit', function(event) {
        const nombreValue = nombreInput.value;
        const codigoValue = codigoInput.value;
        const precioValue = precioInput.value;
        const precioantValue = precioantInput.value;
        const medida_llavesValue = medida_llavesInput.value;
        const contracanastaValue = contracanastaInput.value;
        const marcaValue = marcaInput.value;
        const materialValue = materialInput.value;
        const alimentadorValue = alimentadorInput.value;
        const complementosValue = complementosInput.value;

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
        if (!alimentadorRegex.test(alimentadorValue) || alimentadorValue === '') {
            event.preventDefault();
            spanTextalimentador.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextalimentador.style.display = 'inline';
            alimentadorInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextalimentador.style.display = 'none';
            alimentadorInput.style.border = '';
        }
        // Validar Complementos
        if (!complementosRegex.test(complementosValue) || complementosValue === '') {
            event.preventDefault();
            spanTextcomplementos.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextcomplementos.style.display = 'inline';
            complementosInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextcomplementos.style.display = 'none';
            complementosInput.style.border = '';
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
        // Validar medida_llaves
        if (!medida_llavesRegex.test(medida_llavesValue) || medida_llavesValue === '') {
            event.preventDefault();
            spanTextmedida_llaves.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextmedida_llaves.style.display = 'inline';
            medida_llavesInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextmedida_llaves.style.display = 'none';
            medida_llavesInput.style.border = '';
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

        // Validar Contracanasta
        if (!contracanastaRegex.test(contracanastaValue) || contracanastaValue === '') {
            event.preventDefault();
            spanTextcontracanasta.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextcontracanasta.style.display = 'inline';
            contracanastaInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            spanTextcontracanasta.style.display = 'none';
            contracanastaInput.style.border = '';
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
        const form = document.querySelector(`${modalId} .upKit_install`);

        // Excomplementoses regulares para validación
        const nombreRegex = /^[A-Z][a-z]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+)+$/;
        const codigoRegex = /^[A-Za-z0-9-]{1,15}$/;
        const precioRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/;
        const precioantRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/;
        const medida_llavesRegex = /^\d{1,4}(\.\d{1,4})?x\d{1,4}(\.\d{1,4})?$/;
        const contracanastaRegex = /^\d+$/;
        const marcaRegex = /^(?! )(?:[A-Z][a-záéíóúñÑ]+)(?: (?:[A-Z][a-záéíóúñÑ]+))?(?<! )$/;
        const materialRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
        const alimentadorRegex = /^\d+$/;
        const complementosRegex = /^[A-Z0-9][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z0-9a-záéíóúÁÉÍÓÚñÑ]+){0,59}$/;

        const inputs = form.querySelectorAll('input');
        const spans = form.querySelectorAll('.span_text, .span_codigo, .span_precio, .span_PrecioAnt, .span_marca, .span_medida_llaves, .span_contracanasta, .span_material, .span_alimentador, .span_complementos');

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
                    case 'Medida_llaves_act':
                        regex = medida_llavesRegex;
                        span = form.querySelector('.span_medida_llaves');
                        break;
                    case 'Marca_act':
                        regex = marcaRegex;
                        span = form.querySelector('.span_marca');
                        break;
                    case 'Contracanasta_act':
                        regex = contracanastaRegex;
                        span = form.querySelector('.span_contracanasta');
                        break;
                    case 'Material_act':
                        regex = materialRegex;
                        span = form.querySelector('.span_material');
                        break;
                    case 'Alimentador_act':
                        regex = alimentadorRegex;
                        span = form.querySelector('.span_alimentador');
                        break;
                    case 'Complementos_act':
                        regex = complementosRegex;
                        span = form.querySelector('.span_complementos');
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
