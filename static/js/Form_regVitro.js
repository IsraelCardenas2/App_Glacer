//----------------------------------------- Expreciones regulares Add Pisos y Muros ------------------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.form_reg');
    const nombreInput = form.querySelector('input[name="Nombre"]');
    const precioInput = form.querySelector('input[name="Precio"]');
    const materialInput = form.querySelector('input[name="Material"]');
    const acabadoInput = form.querySelector('input[name="Acabado"]');
    const marcaInput = form.querySelector('input[name="Marca"]');
    const calidadInput = form.querySelector('input[name="Calidad"]');
    const modeloInput = form.querySelector('input[name="PrecioAnt"]');
    const codigoInput = form.querySelector('input[name="Codigo"]');
    const colorInput = form.querySelector('input[name="Color"]');
    const medidaInput = form.querySelector('select[name="Medida"]');
    const contenidoInput = form.querySelector('input[name="Contenido"]');
  
    const spanTextNombre = form.querySelector('.span_text'); // Mensaje de error para Nombre
    const spanTextprecio = form.querySelector('.span_precio'); // Mensaje de error para Precio
    const spanTextmaterial = form.querySelector('.span_material'); // Mensaje de error para el campo Material
    const spanTextAcabado = form.querySelector('.span_acabado'); // Mensaje de error para campo Acabado
    const spanTextmarca = form.querySelector('.span_marca'); // Mensaje de error para el campo Marca
    const spanTextcalidad = form.querySelector('.span_calidad'); // Mensaje de error para el campo Calidad
    const spanTextmodelo = form.querySelector('.span_PrecioAnt'); // Mensaje de error para el campo Modelo
    const spanTextcodigo = form.querySelector('.span_codigo'); // Mensaje de error para el campo Codigo
    const spanTextcolor = form.querySelector('.span_color'); // Mensaje de error para campo color
    const spanTextmedida = form.querySelector('.span_medida'); // Mensaje de error para el campo Medida
    const spanTextcontenido = form.querySelector('.span_contenido'); // Mensaje de error para el campo Contenido

    const nombreRegex = /^[A-Z][a-z]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+)+$/;
    const precioRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/; // Solo números y opcionalmente un decimal
    const materialRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
    const acabadoRegex = /^(?! )(?:[A-Z][a-záéíóú]+)(?: (?:[A-Z][a-z]+))?(?<! )$/;
    const marcaRegex = /^(?! )(?:[A-Z][a-záéíóúñÑ]+)(?: (?:[A-Z][a-záéíóúñÑ]+))?(?<! )$/;
    const calidadRegex = /^(?! )(?:[A-Z][a-z]+)(?: (?:[A-Z][a-z]+))?(?<! )$/;
    const modeloRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/;
    const codigoRegex = /^[A-Za-z0-9-]{1,15}$/;
    const colorRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Z][a-záéíóúÁÉÍÓÚñÑ]+){0,2}$/;
    const medidaRegex = /^\d{1,4}(\.\d{1,4})?x\d{1,4}(\.\d{1,4})?$/;
    const contenidoRegex = /^[0-9]+(\.[0-9]{1,2})?$/;
  
    form.addEventListener('submit', function(event) {
        const nombreValue = nombreInput.value;
        const precioValue = precioInput.value;
  
        const materialValue = materialInput.value;
        const acabadoValue = acabadoInput.value;
        const marcaValue = marcaInput.value;
        const calidadValue = calidadInput.value;
        const modeloValue = modeloInput.value;
        const codigoValue = codigoInput.value;
        const colorValue = colorInput.value;
        const medidaValue = medidaInput.value;
        const contenidoValue = contenidoInput.value;
  
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
  
          // Validar acabado
        if (!acabadoRegex.test(acabadoValue) || acabadoValue === '') {
            event.preventDefault(); // Prevenir envío
  
            // Mostrar mensaje y cambiar borde
            spanTextAcabado.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextAcabado.style.display = 'inline';
            acabadoInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
              // Ocultar mensaje y resetear borde
              spanTextAcabado.style.display = 'none';
              acabadoInput.style.border = '';
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
  
        // Validar Calidad
        if (!calidadRegex.test(calidadValue) || calidadValue === '') {
            event.preventDefault(); // Prevenir envío
  
            // Mostrar mensaje y cambiar borde
            spanTextcalidad.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextcalidad.style.display = 'inline';
            calidadInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextcalidad.style.display = 'none';
            calidadInput.style.border = '';
        }
  
        // Validar Modelo
        if (!modeloRegex.test(modeloValue) || modeloValue === '') {
            event.preventDefault(); // Prevenir envío
  
            // Mostrar mensaje y cambiar borde
            spanTextmodelo.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextmodelo.style.display = 'inline';
            modeloInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextmodelo.style.display = 'none';
            modeloInput.style.border = '';
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
  
        // Validar medida
        if (!medidaRegex.test(medidaValue) || medidaValue === '') {
            event.preventDefault(); // Prevenir envío
  
            // Mostrar mensaje y cambiar borde
            spanTextmedida .style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextmedida.style.display = 'inline';
            medidaInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextmedida.style.display = 'none';
            medidaInput.style.border = '';
        }
  
        // Validar Contenido
        if (!contenidoRegex.test(contenidoValue) || contenidoValue === '') {
            event.preventDefault(); // Prevenir envío
  
            // Mostrar mensaje y cambiar borde
            spanTextcontenido.style.color = 'rgba(224, 16, 16, 0.952)';
            spanTextcontenido.style.display = 'inline';
            contenidoInput.style.border = '2px solid rgba(224, 16, 16, 0.952)';
            isValid = false;
        } else {
            // Ocultar mensaje y resetear borde
            spanTextcontenido.style.display = 'none';
            contenidoInput.style.border = '';
        }
  
  
        // Si ambos son válidos, se enviará el formulario
        if (isValid) {
            // Aquí puedes manejar el envío del formulario si es necesario
        }
    });
  });