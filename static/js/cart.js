var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

function saveCartToLocalStorage() {
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
}

function updateCartDisplay() {
    var cartContainer = document.getElementById('cart-container');
    var cartItemsElement = cartContainer.querySelector('.cart-items');

    cartItemsElement.innerHTML = '';

    cartItems.forEach(function (item, index) {
        var itemElement = document.createElement('div');
        itemElement.classList.add('cart-item');

        var totalPrice = (item.price * item.quantity).toFixed(2);
        var priceString = item.type === 'pizza' || item.type === 'drinks' || item.type === 'sides' ||item.type=='desserts' ||item.type=='mealdeals'
            ? `$${totalPrice}`
            : `$${item.price} each`;

        var additionalDetails = '';
        if (item.size) additionalDetails += item.size + ' - ';
        if (item.base) additionalDetails += item.base + ' - ';

        itemElement.innerHTML = `
            <span>${item.name} - ${additionalDetails}${priceString}</span>
            <div class="quantity-controls">
                <button onclick="changeQuantity(${index}, 'subtract')">-</button>
                <input type="number" class="quantity-input" value="${item.quantity}" min="1" id="quantity-input-${index}">
                <button onclick="changeQuantity(${index}, 'add')">+</button>
            </div>
            <button class="remove-button" onclick="removeItem(${index})">Remove</button>
        `;

        cartItemsElement.appendChild(itemElement);
    });

    var totalPriceElement = cartContainer.querySelector('.total-price');
    var totalPrice = cartItems.reduce(function (total, item) {
        return total + item.price * item.quantity;
    }, 0);
    totalPriceElement.textContent = `Total: $${totalPrice.toFixed(2)}`;
}

document.addEventListener('DOMContentLoaded', function () {
    updateCartDisplay();
});

function changeQuantity(index, action) {
    var quantityInput = document.getElementById(`quantity-input-${index}`);
    var currentQuantity = parseInt(quantityInput.value);

    if (action === 'add') {
        quantityInput.value = currentQuantity + 1;
    } else if (action === 'subtract' && currentQuantity > 1) {
        quantityInput.value = currentQuantity - 1;
    }

    cartItems[index].quantity = parseInt(quantityInput.value);
    saveCartToLocalStorage();
    updateCartDisplay();
}

function removeItem(index) {
    cartItems.splice(index, 1);
    saveCartToLocalStorage();
    updateCartDisplay();
}

function clearCart() {
    cartItems = [];
    saveCartToLocalStorage();
    updateCartDisplay();
}

function addToCart(button) {
    var productName = button.getAttribute('data-name');
    var productPrice = parseFloat(button.getAttribute('data-price'));
    var itemType = button.getAttribute('data-type');

    // Additional details for side
    var sizeSelect = button.parentElement.querySelector('.size-select');
    var selectedSize = sizeSelect ? sizeSelect.options[sizeSelect.selectedIndex].value : null;
    var sizePrice = sizeSelect ? parseFloat(sizeSelect.options[sizeSelect.selectedIndex].getAttribute('data-price')) : 0;

    // Calculate total product price
    var totalProductPrice = productPrice + sizePrice;

    var cartItem = {
        type: itemType,
        name: productName,
        size: selectedSize,
        price: totalProductPrice,
        quantity: 1
    };

    cartItems.push(cartItem);
    saveCartToLocalStorage();
    updateCartDisplay();
}
