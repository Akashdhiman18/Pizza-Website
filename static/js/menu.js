// Function to toggle cart container
const cartIconBtn = document.querySelector('.cart-icon-btn');
cartIconBtn.addEventListener('click', function() {
    const cartContainer = document.querySelector('.cart-container');
    cartContainer.classList.toggle('open');
});

function checkout() {
    // Replace '/cg' with the actual URL of your checkout page
    window.location.href = '/checkout';
}

function addToCart(pizzaName) {
    // Get selected size and base from the dropdowns
    const sizeSelect = document.querySelector('.size-select');
    const baseSelect = document.querySelector('.base-select');
    const selectedSize = sizeSelect.options[sizeSelect.selectedIndex];
    const selectedBase = baseSelect.options[baseSelect.selectedIndex];

    // Calculate the total price based on the selected size and base prices
    const totalPrice = parseFloat(selectedSize.dataset.price) + parseFloat(selectedBase.dataset.price);

    // Create an object to send to the server
    const data = {
        pizzaName: pizzaName,
        size: selectedSize.value,
        base: selectedBase.value,
        totalPrice: totalPrice
    };

    // Send an AJAX request to add the item to the cart
    $.ajax({
        type: 'POST',
        url: '/add_to_cart',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(data),
        success: function (response) {
            alert('Item added to cart!');
            updateCart();  // Call a function to update the cart display
        },
        error: function (error) {
            console.log(error);
        }
    });
}

// Function to update the cart display
function updateCart() {
    // Make an AJAX request to get the current cart items
    $.ajax({
        type: 'GET',
        url: '/get_cart_items',
        success: function (response) {
            // Assuming the response is a JSON array of cart items
            const cartItems = response.cartItems;

            // Update the HTML to display the cart items
            const cartContainer = document.querySelector('.cart-items');
            cartContainer.innerHTML = '';  // Clear previous items

            // Loop through the cart items and create HTML elements for each
            cartItems.forEach(item => {
                const cartItemElement = document.createElement('div');
                cartItemElement.classList.add('cart-item');

                cartItemElement.innerHTML = `
                    <span>${item.name} - ${item.size} - ${item.base}</span>
                    <span>${item.price}</span>
                    <button onclick="removeFromCart(${item.id})">Remove</button>
                `;

                cartContainer.appendChild(cartItemElement);
            });
        },
        error: function (error) {
            console.log(error);
        }
    });
}

// Function to remove an item from the cart
function removeFromCart(itemId) {
    // Make an AJAX request to remove the item from the cart
    $.ajax({
        type: 'POST',
        url: '/remove_from_cart',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ itemId: itemId }),
        success: function (response) {
            alert('Item removed from cart!');
            updateCart();  // Call updateCart after removing an item
        },
        error: function (error) {
            console.log(error);
        }
    });
}