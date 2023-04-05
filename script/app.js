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




