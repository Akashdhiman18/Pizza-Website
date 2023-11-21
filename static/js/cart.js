
    var cartItems = [];
    var Drink = [];
    
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
        var totalProductPrice = productPrice + parseFloat(sizeSelect.options[sizeSelect.selectedIndex].getAttribute('data-price')) + parseFloat(baseSelect.options[baseSelect.selectedIndex].getAttribute('data-price'));

        // Create an object to represent the item
        var cartItem = {
            name: productName,
            size: selectedSize,
            base: selectedBase,
            price: totalProductPrice
        };

        var Drink = {
            
        }
        // Add the item to the cart array
        cartItems.push(cartItem);

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
        cartItems.forEach(function (item) {
            var itemElement = document.createElement('div');
            itemElement.innerHTML = `${item.name} - ${item.size} - ${item.base}: $${item.price.toFixed(2)}`;
            cartItemsElement.appendChild(itemElement);
        });

        // Calculate and display the total price
        var totalPriceElement = cartContainer.querySelector('.total-price');
        var totalPrice = cartItems.reduce(function (total, item) {
            return total + item.price;
        }, 0);
        totalPriceElement.textContent = `Total: $${totalPrice.toFixed(2)}`;
    }

    function checkout() {
        // Implement the checkout logic here
        // You can send the cartItems array to the server or perform any other necessary actions
        // For now, let's just log the cart items to the console
        window.location.href = '/checkout';
        console.log(cartItems);
    }
 
    