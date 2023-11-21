
     // Function to toggle cart container (json file)
     const cartIconBtn = document.querySelector('.cart-icon-btn');
     cartIconBtn.addEventListener('click', function() {
         const cartContainer = document.querySelector('.cart-container');
         cartContainer.classList.toggle('open');
     });
     
     function checkout() {
         // Replace '/cg' with the actual URL of your checkout page
         window.location.href = '/checkout';
     }
     
     
     function addToCart(button) {
        const itemName = button.getAttribute('data-name');
        const itemPriceAttr = button.getAttribute('data-price');
        
        // Check if itemPriceAttr is a valid number
        if (!itemPriceAttr || isNaN(itemPriceAttr)) {
            console.error(`Invalid or missing data-price attribute for ${itemName}`);
            return;
        }
    
        const itemPrice = parseFloat(itemPriceAttr);
        const itemSize = document.querySelector('.size-select').value;
        const itemBase = document.querySelector('.base-select').value;
        const itemQuantity = parseInt(document.querySelector('.quantity-input').value) || 1;
    
        const cartItem = {
            name: itemName,
            size: itemSize,
            base: itemBase,
            price: itemPrice,
            quantity: itemQuantity,
        };
    
        updateCart(cartItem); 
    }
    
     
     function updateCart(cartItem) {
        const cartItemsContainer = document.querySelector('.cart-items');
        const cartItemDiv = document.createElement('div');
        const totalDiv = document.querySelector('.total-price');
    
        // Calculate item total price
        const itemTotal = cartItem.price * cartItem.quantity;
    
        // Display item in the cart
        cartItemDiv.innerHTML = `<p>${cartItem.quantity} x ${cartItem.name} - $${itemTotal.toFixed(2)}</p>`;
        cartItemsContainer.appendChild(cartItemDiv);
    
        // Update total price
        const currentTotal = parseFloat(totalDiv.innerText.replace('$', '')) || 0;
        const newTotal = currentTotal + itemTotal;
    
        // Update totalDiv with the new total
        totalDiv.innerText = `$${newTotal.toFixed(2)}`; 
    } 
    