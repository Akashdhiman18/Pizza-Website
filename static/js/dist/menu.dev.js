"use strict";

// Function to toggle cart container (json file)
var cartIconBtn = document.querySelector('.cart-icon-btn');
cartIconBtn.addEventListener('click', function () {
  var cartContainer = document.querySelector('.cart-container');
  cartContainer.classList.toggle('open');
});

function checkout() {
  // Replace '/cg' with the actual URL of your checkout page
  window.location.href = '/checkout';
}

function addToCart(button) {
  var itemName = button.getAttribute('data-name');
  var itemPriceAttr = button.getAttribute('data-price'); // Check if itemPriceAttr is a valid number

  if (!itemPriceAttr || isNaN(itemPriceAttr)) {
    console.error("Invalid or missing data-price attribute for ".concat(itemName));
    return;
  }

  var itemPrice = parseFloat(itemPriceAttr);
  var itemSize = document.querySelector('.size-select').value;
  var itemBase = document.querySelector('.base-select').value;
  var itemQuantity = parseInt(document.querySelector('.quantity-input').value) || 1;
  var cartItem = {
    name: itemName,
    size: itemSize,
    base: itemBase,
    price: itemPrice,
    quantity: itemQuantity
  };
  updateCart(cartItem);
}

function updateCart(cartItem) {
  var cartItemsContainer = document.querySelector('.cart-items');
  var cartItemDiv = document.createElement('div');
  var totalDiv = document.querySelector('.total-price'); // Calculate item total price

  var itemTotal = cartItem.price * cartItem.quantity; // Display item in the cart

  cartItemDiv.innerHTML = "<p>".concat(cartItem.quantity, " x ").concat(cartItem.name, " - $").concat(itemTotal.toFixed(2), "</p>");
  cartItemsContainer.appendChild(cartItemDiv); // Update total price

  var currentTotal = parseFloat(totalDiv.innerText.replace('$', '')) || 0;
  var newTotal = currentTotal + itemTotal; // Update totalDiv with the new total

  totalDiv.innerText = "$".concat(newTotal.toFixed(2));
}
//# sourceMappingURL=menu.dev.js.map
