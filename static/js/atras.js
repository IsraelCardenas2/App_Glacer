function goBack() {
    window.history.back();
}

document.addEventListener("DOMContentLoaded", function() {
    // Obtener todos los detalles en el menú
    const detailsElements = document.querySelectorAll('.barra_menu details');
    
    // Añadir un evento de apertura (open) a cada <details>
    detailsElements.forEach((details) => {
        details.addEventListener('toggle', function() {
            // Si este <details> se abre, cerrar los demás
            if (details.open) {
                detailsElements.forEach((otherDetails) => {
                    if (otherDetails !== details) {
                        otherDetails.removeAttribute('open');
                    }
                });
            }
        });
    });

    // Añadir un evento de clic en el documento para cerrar todos los detalles
    document.addEventListener('click', function(event) {
        // Verificar si el clic fue fuera de los detalles
        const isClickInsideDetails = Array.from(detailsElements).some(details => details.contains(event.target));
        
        if (!isClickInsideDetails) {
            // Si el clic fue fuera de cualquier <details>, cerramos todos
            detailsElements.forEach((details) => {
                details.removeAttribute('open');
            });
        }   
    });

})



//------------------------------ Sección de código para la barra de búsqueda en catalogos ---------------

document.getElementById('search-bar').addEventListener('input', function() {
    let query = this.value.toLowerCase(); // Obtener el valor ingresado
    let products = document.querySelectorAll('.product-card'); // Obtener todos los productos
    let noResultsMessage = document.getElementById('no-results-message');
    let searchQueryElement = document.getElementById('search-query');
    
    let foundResults = false;

    products.forEach(function(product) {
        let productName = product.querySelector('h3').innerText.toLowerCase();
        if (productName.includes(query)) {
            product.style.display = ''; // Mostrar el producto
            foundResults = true;
        } else {
            product.style.display = 'none'; // Ocultar el producto
        }
    });

    // Mostrar mensaje de "Sin resultados" si no se encuentra nada
    if (!foundResults && query !== '') {
        noResultsMessage.style.display = 'block';
        searchQueryElement.innerText = query; // Mostrar el texto de búsqueda
    } else {
        noResultsMessage.style.display = 'none'; // Ocultar el mensaje si hay resultados
    }
});