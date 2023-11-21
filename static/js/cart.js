var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];















function addToCart(button) {
    // Get the product details from the button's data attributes
    var productName = button.getAttribute('data-name');
    var productPrice = parseFloat(button.getAttribute('data-price'));

    // Get the selected size and base
    var sizeSelect = button.parentElement.querySelector('.size-select');
    var baseSelect = button.parentElement.querySelector('.base-select');
    var selectedSize = sizeSelect.options[sizeSelect.selectedIndex].value;
    var selectedBase = baseSelect.options[baseSelect.selectedIndex].value;

    // Calculate the total price based on size and base
    var totalProductPrice =
        productPrice +
        parseFloat(sizeSelect.options[sizeSelect.selectedIndex].getAttribute('data-price')) +
        parseFloat(baseSelect.options[baseSelect.selectedIndex].getAttribute('data-price'));

    // Create an object to represent the item
    var cartItem = {
        name: productName,
        size: selectedSize,
        base: selectedBase,
        price: totalProductPrice,
        quantity: 1 // Set initial quantity to 1 when adding to cart
    };

    // Add the item to the cart array
    cartItems.push(cartItem);

    saveCartToLocalStorage();
    // Call a function to update the cart display
    updateCartDisplay();
}

function updateCartDisplay() {
    // Get the cart container and items element
    var cartContainer = document.getElementById('cart-container');
    var cartItemsElement = cartContainer.querySelector('.cart-items');

    // Clear the existing content
    cartItemsElement.innerHTML = '';

    // Loop through the items in the cart and display them
    cartItems.forEach(function (item, index) {
        var itemElement = document.createElement('div');
        itemElement.classList.add('cart-item');

        // Display item details
        itemElement.innerHTML = `
            <span>${item.name} - ${item.size} - ${item.base}: $${(item.price * item.quantity).toFixed(2)}</span>
            <div class="quantity-controls">
            <button onclick="changeQuantity(${index}, 'subtract')">-</button>
            <input type="number" class="quantity-input" value="${item.quantity}" min="1" id="quantity-input-${index}">
            <button onclick="changeQuantity(${index}, 'add')">+</button>
            </div>
            <button class="remove-button" onclick="removeItem(${index})">Remove</button>
        `;

        cartItemsElement.appendChild(itemElement);
    });

    // Calculate and display the total price
    var totalPriceElement = cartContainer.querySelector('.total-price');
    var totalPrice = cartItems.reduce(function (total, item) {
        return total + item.price * item.quantity;
    }, 0);
    totalPriceElement.textContent = `Total: $${totalPrice.toFixed(2)}`;
}

function changeQuantity(index, action) {
    var quantityInput = document.getElementById(`quantity-input-${index}`);
    var currentQuantity = parseInt(quantityInput.value);

    if (action === 'add') {
        quantityInput.value = currentQuantity + 1;
    } else if (action === 'subtract' && currentQuantity > 1) {
        quantityInput.value = currentQuantity - 1;
    }

    // Update the quantity in the cart array
    cartItems[index].quantity = parseInt(quantityInput.value);

    saveCartToLocalStorage();
    // Update the total price and refresh the display
    updateCartDisplay();
}

function removeItem(index) {
    cartItems.splice(index, 1);

    saveCartToLocalStorage();
    updateCartDisplay();
}

function clearCart() {
    var cartItemsElement = document.querySelector('.cart-items');
    cartItemsElement.innerHTML = '';
    cartItems = [];

    // Save empty cart to localStorage
    saveCartToLocalStorage();

    updateCartDisplay();
}

function saveCartToLocalStorage() {
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
}

document.addEventListener('DOMContentLoaded', function () {
    updateCartDisplay();
});
