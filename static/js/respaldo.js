

// Función para realizar la búsqueda
document.getElementById('search-input').addEventListener('input', function () {
    let input = document.getElementById('search-input').value.trim();
    let regex = /^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]*$/;  // Expresión regular personalizada (puedes modificarla)
    let noResultsMessage = document.getElementById('no-results');
    let tableRows = document.querySelectorAll('#product-table-body tr');
    
    // Validación de la búsqueda
    if (!regex.test(input) && input !== "") {
        noResultsMessage.textContent = "Entrada no válida";
        noResultsMessage.style.display = 'block';
        return;
    } else {
        noResultsMessage.style.display = 'none';
    }

    let found = false;
    // Filtrar los registros de la tabla
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
            row.style.display = '';
            found = true;
        } else {
            row.style.display = 'none';
        }
    });

    // Si no se encuentran resultados, mostrar el mensaje de "No hay coincidencias"
    if (!found && input !== "") {
        noResultsMessage.style.display = 'block';
    } else {
        noResultsMessage.style.display = 'none';
    }
});







// ----------------------------------- Páginación y Buscador 95% funcioanl ------------------------------------------

// Variables globales
let currentPage = 1;
const recordsPerPage = 5;
let filteredRecords = [];

// Obtener los registros de la tabla
const tableRows = document.querySelectorAll('#product-table-body tr');

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

    // Agregar los botones de números
    for (let i = 1; i <= totalPages; i++) {
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
    let regex = /^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]*$/;  // Expresión regular personalizada (puedes modificarla)
    let noResultsMessage = document.getElementById('no-results');

    // Validación de la búsqueda
    if (!regex.test(input) && input !== "") {
        noResultsMessage.textContent = "Entrada no válida";
        noResultsMessage.style.display = 'block';
        filteredRecords = [];
        updatePagination([]);
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
        noResultsMessage.style.display = 'block';
    } else {
        noResultsMessage.style.display = 'none';
    }

    // Recalcular el total de páginas y mostrar la página actual
    currentPage = 1;  // Resetear a la primera página
    showPage(currentPage);
});

// Inicializar la paginación con los registros completos
showPage(currentPage);