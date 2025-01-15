

document.addEventListener('DOMContentLoaded', function () {
    // Obtiene el elemento <span> que contiene el privilegio
    const privilegioSpan = document.getElementById('span_privilegio');
    
    if (privilegioSpan) {
        const privilegio = privilegioSpan.textContent.trim(); // Obtiene y limpia el texto
        
        // Obtiene la columna y la fila por sus IDs
        const columnaAcciones = document.getElementById('Colu_Acc');
        const filaAcciones = document.getElementById('Col_data');
        
        // Verifica el privilegio y aplica las acciones correspondientes
        if (privilegio === 'Subadministrador') {
            console.log(privilegio)
            if (columnaAcciones) columnaAcciones.style.display = 'none'; // Oculta la columna
            if (filaAcciones) {
                // Oculta todas las celdas de la fila
                const filas = document.querySelectorAll(`#product-table-body tr td:nth-child(${columnaAcciones.cellIndex + 1})`);
                filas.forEach(fila => fila.style.display = 'none');
            }
        } else if (privilegio === 'Administrador') {
            console.log(privilegio)
            if (columnaAcciones) columnaAcciones.style.display = ''; // Asegura que la columna sea visible
            if (filaAcciones) {
                const filas = document.querySelectorAll(`#product-table-body tr td:nth-child(${columnaAcciones.cellIndex + 1})`);
                filas.forEach(fila => fila.style.display = '');
            }
        }
    }
});






document.addEventListener('DOMContentLoaded', function () {
    // Obtiene el elemento <span> que contiene el privilegio
    const privilegioSpan = document.getElementById('span_privilegio');
    
    if (privilegioSpan) {
        const privilegio = privilegioSpan.textContent.trim(); // Obtiene y limpia el texto
        
        // Obtiene la columna y la fila por sus IDs
        const btn_usersGestion = document.getElementById('Btn-Users');
        
        // Verifica el privilegio y aplica las acciones correspondientes
        if (privilegio === 'Subadministrador') {
            console.log(privilegio)
            if (btn_usersGestion) btn_usersGestion.style.display = 'none'; // Oculta el boton
        } else if (privilegio === 'Administrador') {
            console.log(privilegio)
            if (btn_usersGestion) btn_usersGestion.style.display = ''; 
        }
    }
});

















function confirmDelete(url) {
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

//------------------------------------ Boton Cerrar Sesión --------------------------------------------

document.addEventListener('DOMContentLoaded', function() {
    const off = document.getElementById('Cerrar_sesion');
    const icon = document.getElementById('ckn');

    icon.addEventListener('click', function() {
        if (off.classList.contains('hiddentico')) {
            off.classList.remove('hiddentico'); // Muestra el botón
        } else {
            off.classList.add('hiddentico'); // Oculta el botón
        }
    });
});

// ---------------------------------------------------------- Formularios Multi pasos --------------------------------------------------------

document.addEventListener("DOMContentLoaded", function () {
    const steps = document.querySelectorAll(".step");
    const nextButtons = document.querySelectorAll(".next");
    const prevButtons = document.querySelectorAll(".prev");
    let currentStep = 0;
  
    // Muestra el paso actual
    function showStep(step) {
      steps.forEach((s, index) => {
        s.classList.toggle("active", index === step);
      });
    }
  
    // Manejo de clic en el botón "Siguiente"
    nextButtons.forEach((btn) => {
      btn.addEventListener("click", function () {
        if (currentStep < steps.length - 1) {
          currentStep++;
          showStep(currentStep);
        }
      });
    });
  
    // Manejo de clic en el botón "Anterior"
    prevButtons.forEach((btn) => {
      btn.addEventListener("click", function () {
        if (currentStep > 0) {
          currentStep--;
          showStep(currentStep);
        }
      });
    });
  
    // Inicializar el formulario mostrando el primer paso
    showStep(currentStep);
  });

// ----------------------------------------- Instrucciones para el fitro de búsqueda y paginado -----------------------------------

// Variables globales
let currentPage = 1;
const recordsPerPage = 10;
let filteredRecords = [];

// Obtener los registros de la tabla
const tableRows = document.querySelectorAll('#product-table-body tr');
const noResultsMessage = document.getElementById('no-results');
const tableBody = document.getElementById('product-table-body'); // Cuerpo de la tabla (<tbody>)

// Función para mostrar los registros según la página
function showPage(page) {
    const startIndex = (page - 1) * recordsPerPage;
    const endIndex = startIndex + recordsPerPage;

    // Filtrar los registros visibles según la búsqueda
    const recordsToDisplay = filteredRecords.length > 0 ? filteredRecords : Array.from(tableRows);

    // Ocultar todos los registros
    recordsToDisplay.forEach((row, index) => {
        if (index >= startIndex && index < endIndex) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });

    // Actualizar la paginación
    updatePagination(recordsToDisplay);
}

// Función para actualizar los números de la paginación
function updatePagination(recordsToDisplay) {
    const totalPages = Math.ceil(recordsToDisplay.length / recordsPerPage);
    const paginationNumbers = document.getElementById('pagination-numbers');
    paginationNumbers.innerHTML = ''; // Limpiar números anteriores

    // Determinar el rango de páginas que se mostrarán (5 páginas a la vez)
    let startPage = Math.max(1, currentPage - 2); // 2 páginas antes de la actual
    let endPage = Math.min(totalPages, currentPage + 2); // 2 páginas después de la actual

    // Mostrar solo las páginas dentro del rango calculado
    for (let i = startPage; i <= endPage; i++) {
        const pageNumber = document.createElement('div');
        pageNumber.classList.add('pagination-number');
        pageNumber.textContent = i;

        // Activar la página actual
        if (i === currentPage) {
            pageNumber.classList.add('active');
        }

        // Establecer el evento de clic
        pageNumber.addEventListener('click', () => {
            currentPage = i;
            showPage(currentPage);
        });

        paginationNumbers.appendChild(pageNumber);
    }

    // Mostrar u ocultar los botones de avance y retroceso
    document.getElementById('prev-page').style.display = currentPage > 1 ? 'inline-block' : 'none';
    document.getElementById('Pagina_sig').style.display = currentPage < totalPages ? 'inline-block' : 'none';
}

// Función para avanzar a la siguiente página
function nextPagell() {
    const recordsToDisplay = filteredRecords.length > 0 ? filteredRecords : Array.from(tableRows);
    if (currentPage < Math.ceil(recordsToDisplay.length / recordsPerPage)) {
        currentPage++;
        showPage(currentPage);
    }
}

// Función para retroceder a la página anterior
function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        showPage(currentPage);
    }
}

// Configurar los botones de avanzar y retroceder
document.getElementById('Pagina_sig').addEventListener('click', nextPagell);
document.getElementById('prev-page').addEventListener('click', prevPage);

// Función para realizar la búsqueda
document.getElementById('search-input').addEventListener('input', function () {
    let input = document.getElementById('search-input').value.trim();
    let regex = /^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]*$/;  // Expresión regular personalizada

    // Validación de la búsqueda
    if (!regex.test(input) && input !== "") {
        noResultsMessage.textContent = "Entrada no válida";
        noResultsMessage.style.display = 'block';
        filteredRecords = [];
        updatePagination([]); // Actualizar paginación con los registros filtrados vacíos
        showPage(1);
        return;
    } else {
        noResultsMessage.style.display = 'none';
    }

    // Filtrar los registros de la tabla
    filteredRecords = [];
    tableRows.forEach(function(row) {
        let columns = row.getElementsByTagName('td');
        let matchFound = false;

        // Verificar si alguna columna contiene el término de búsqueda
        for (let i = 0; i < columns.length; i++) {
            if (columns[i].textContent.toLowerCase().includes(input.toLowerCase())) {
                matchFound = true;
                break;
            }
        }

        // Mostrar/ocultar filas basadas en el filtro
        if (matchFound) {
            filteredRecords.push(row);
            row.style.display = '';  // Mostrar la fila
        } else {
            row.style.display = 'none';  // Ocultar la fila
        }
    });

    // Si no se encuentran resultados, mostrar el mensaje de "No hay coincidencias"
    if (filteredRecords.length === 0) {
        noResultsMessage.textContent = `Sin resultados para: ${input}`;
        noResultsMessage.style.display = 'block';
        noResultsMessage.style.color = 'red';
        tableBody.style.display = 'none';  // Ocultar el <tbody>
    } else {
        noResultsMessage.style.display = 'none';
        tableBody.style.display = 'table-row-group';  // Mostrar el <tbody>
    }

    // Recalcular el total de páginas y mostrar la página actual
    currentPage = 1;  // Resetear a la primera página
    showPage(currentPage);
});

// Inicializar la paginación con los registros completos
showPage(currentPage);


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

  // Expresiones regulares personalizables
  const nombreRegex = /^[A-Z][a-z]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+)+$/;
  const precioRegex = /^(?:[1-9][0-9]{2,}|1000+)(?:\.[0-9]{1,2})?$/; // Solo números y opcionalmente un decimal
  const materialRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
  const acabadoRegex = /^[A-Z][a-záéíóúÁÉÍÓÚñÑ]+(\s[A-Za-záéíóúÁÉÍÓÚñÑ]+){0,49}$/;
  const marcaRegex = /^(?! )(?:[A-Z][a-z]+)(?: (?:[A-Z][a-z]+))?(?<! )$/;
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



//------------------------- Expreciones Regulares para los forms de actualización de Pis y Mur ---------------------
