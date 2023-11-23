// Function to update the cart content and total
function updateCart() {
    var cartContent = document.getElementById('cart-content');
    var cartItems = getCartItems();

    // Clear previous content
    cartContent.innerHTML = '';

    // Initialize variables for cart details
    var cartItemName = '';
    var cartQuantity = 0;
    var cartTotalPrice = 0;

    // Display cart items in the cart
    cartItems.forEach(function (item) {
        var cartItem = document.createElement('p');
        var itemPrice = item.price * item.quantity;
        cartItem.textContent = `${item.name} x ${item.quantity}  Price : $${itemPrice.toFixed(2)}`;
        cartContent.appendChild(cartItem);

        // Update cart details
        cartItemName += item.name + ', ';
        cartQuantity += item.quantity;
        cartTotalPrice += itemPrice;
    });

    // Set values of hidden fields
    document.getElementById('cart-item-name').value = cartItemName.slice(0, -2); // Remove the trailing comma and space
    document.getElementById('cart-quantity').value = cartQuantity;
    document.getElementById('cart-total-price').innerText = '$' + cartTotalPrice.toFixed(2); // Update the cart total price display

    // Log the total price to console for debugging
    console.log('Cart Total Price: $' + cartTotalPrice.toFixed(2));
}

updateCart();


function getCartItems() {
    var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

    return cartItems;
}

function addToCart(item) {
    var cartItems = getCartItems();
    var existingItem = cartItems.find(cartItem => cartItem.name === item.name);

    if (existingItem) {
        
        existingItem.quantity += 1;
    } else {
       
        cartItems.push({ ...item, quantity: 1 });
    }

   
    localStorage.setItem('cartItems', JSON.stringify(cartItems));


    updateCart();
}

function submitForm() {
    event.preventDefault(); // Prevent the form from submitting in the traditional way

    // Fetch API to send form data to the server
    fetch('/checkout_form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            price: parseFloat(document.getElementById('cart-total-price').innerText.replace('$', '')),
            item_name: document.getElementById('cart-item-name').value,
            quantity: parseInt(document.getElementById('cart-quantity').value),
            address: document.getElementById('adr').value,
            phone: document.getElementById('phone').value,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        console.log(data);
        // You can redirect to another page or update the UI as needed
    })
    .catch((error) => {
        // console.error('Error:', error);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById('checkouts-form');
    form.addEventListener('submit', function(event) {
        // This is optional, but you can log to see if the event is being triggered
        console.log('Form submitted');
    });
});
function goBack() {
    window.history.back();
}

    
    
    