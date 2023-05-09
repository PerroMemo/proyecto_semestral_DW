

const carrito = document.getElementById('carrito');
const elementos = document.getElementById('lista');
const lista = document.querySelector('#lista-carrito tbody');
const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

cargarEventListeners();

function cargarEventListeners() {
  elementos.addEventListener('click', comprarElemento);
  carrito.addEventListener('click', eliminarElemento);
  vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
  document.addEventListener('DOMContentLoaded', leerLocalStorage);
}

function comprarElemento(e) {
    e.preventDefault();
    if(e.target.classList.contains('agregar-carrito')) {
        const elemento = e.target.parentElement.parentElement;
        leerDatosElemento(elemento);
    }
}

function leerDatosElemento(elemento) {
    const infoElemento = {
      imagen : elemento.querySelector('img').src,
      titulo : elemento.querySelector('h2').textContent,
      precio : elemento.querySelector('.precio').textContent,
      id: elemento.querySelector('a').getAttribute('data-id')
    }
    
    insertarCarrito(infoElemento);

}

function insertarCarrito(elemento) {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>
              <img src="${elemento.imagen}" width=100>
        </td>

        <td>
            ${elemento.titulo}
        </td>
        <td>
            ${elemento.precio}
        </td>
        <td>
            <a herf="#"  class="borrar"  data-id=${elemento.id}>X</a>
        </td>    
    `;
    lista.appendChild(row);
    guardarElementoLocalStorage(elemento);

}

function eliminarElemento(e) {
    
    e.preventDefault();

    let elemento,
        elementoId;
    
    if (e.target.classList.contains('borrar')){

        e.target.parentElement.parentElement.remove();
        elemento = e.target.parentElement.parentElement;
        elementoId = elemento.querySelector('a').getAttribute('data-id');
    }

    eliminarElementoLocalStorage(elementoId)

}

function vaciarCarrito() {
    while(lista.firstChild) {
        lista.removeChild(lista.firstChild);
    }

    vaciarLocalStorage();
    return false;

}

function guardarElementoLocalStorage(elemento) {
    
    let elementos;

    elementos = obtenerelementosLocalStorage();

    elementos.push(elemento);

    localStorage.setItem('elementos', JSON.stringify(elementos));
}

function obtenerelementosLocalStorage() {
    let elementosLS;

    if(localStorage.getItem('elementos') == null) {
        elementosLS = [];
    } else {
        elementosLS = JSON.parse(localStorage.getItem('elementos'));
    }
    return elementosLS;
}

function leerLocalStorage() {
     
    let elementosLS;
    
    elementosLS = obtenerelementosLocalStorage();

    elementosLS.forEach(function(elemento){

        const row = document.createElement('tr');
        row.innerHTML = `
            <td>
                  <img src="${elemento.imagen}" width=100>
            </td>
    
            <td>
                ${elemento.titulo}
            </td>
            <td>
                ${elemento.precio}
            </td>
            <td>
                <a herf="#"  class="borrar"  data-id=${elemento.id}>X</a>
            </td>    
        `;
        lista.appendChild(row);
    });
}

function eliminarElementoLocalStorage(elemento) {
    let elementosLS;

    elementosLS = obtenerelementosLocalStorage();
    elementosLS.forEach(function(elementoLS, main){

        if(elementoLS.id == elemento){
           elementoLS.splice(main, 1);
        }
    });

    localStorage.setItem('elementos', JSON.stringify(elementosLS));
}

function vaciarLocalStorage() {
    localStorage.clear();
}

// Crea un objeto de carrito vacío
let cart = {};

// Obtén los botones "Agregar al carrito" y agrega eventos de clic a cada uno
let addToCartButtons = document.querySelectorAll('.add-to-cart');
addToCartButtons.forEach(button => {
  button.addEventListener('click', () => {
    let product = button.dataset.product;
    if (cart[product]) {
      cart[product] += 1;
    } else {
      cart[product] = 1;
    }
    updateCart();
  });
});

// Obtén el botón "Vaciar carrito" y agrega un evento de clic
let emptyCartButton = document.querySelector('#empty-cart');
emptyCartButton.addEventListener('click', () => {
  cart = {};
  updateCart();
});

// Actualiza el contenido del carrito
function updateCart() {
  let cartBody = document.querySelector('#cart-body');
  let cartTotal = document.querySelector('#cart-total');
  let cartRows = '';
  let total = 0;
  for (let product in cart) {
    let quantity = cart[product];
    let price = 0;
    // Asigna el precio según el producto
    if (product === 'producto1') {
      price = 10;
    } else if (product === 'producto2') {
      price = 20;
    }
    let subtotal = price * quantity;
    total += subtotal;
    cartRows += `
      <tr>
        <td>${product}</td>
        <td>${quantity}</td>
        <td>$${price}</td>
        <td>$${subtotal}</td>
        <td><button class="remove-item" data-product="${product}">Eliminar</button></td>
      </tr>
    `;
  }
  cartBody.innerHTML = cartRows;
  cartTotal.innerHTML = `$${total}`;
  // Obtén los botones "Eliminar" y agrega eventos de clic a cada uno
  let removeItemButtons = document.querySelectorAll('.remove-item');
  removeItemButtons.forEach(button => {
    button.addEventListener('click', () => {
      let product = button.dataset.product;
      if (cart[product] > 1) {
        cart[product] -= 1;
      } else {
        delete cart[product];
      }
      updateCart();
    });
  });
}

// Obtén el botón "Pagar" y agrega un evento de clic
let checkoutButton = document.querySelector('#checkout');
checkoutButton.addEventListener('click', () => {
  alert('¡Gracias por su compra!');
});





