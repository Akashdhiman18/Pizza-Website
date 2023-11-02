document.addEventListener("DOMContentLoaded", function() {
    // Get all the size dropdown buttons and size select elements
    const sizeDropdownBtns = document.querySelectorAll('.size-dropdown-btn');
    const sizeSelects = document.querySelectorAll('.size-select');
    // Add event listener for each size select element
    sizeSelects.forEach((select, index) => {
        select.addEventListener('change', function() {
            const selectedSize = select.value;
            sizeDropdownBtns[index].textContent = 'Size (' + selectedSize + ')';
        });
    });
    // Get all the base dropdown buttons and base select elements
    const baseDropdownBtns = document.querySelectorAll('.base-dropdown-btn');
    const baseSelects = document.querySelectorAll('.base-select');

    // Add event listener for each base select element
    baseSelects.forEach((select, index) => {
        select.addEventListener('change', function() {
            const selectedBase = select.value;
            baseDropdownBtns[index].textContent = 'Base (' + selectedBase + ')';
        });
    });
    // Get all the cart buttons and cart items container
const cartButtons = document.querySelectorAll('.cart-button');
const cartItemsContainer = document.querySelector('.cart-items');

// Array to store selected items
let cartItems = [];

// Define a lookup table for prices based on size and base options
const priceLookup = {
    small: {
        thin: 11,  // Small + Thin Crust: $5 + $6 = $11
        thick: 18,  // Small + Thick Crust: $5 + $13 = $18
        'Gluten-Free': 30  // Small + Gluten-Free: $5 + $25 = $30
    },
    Medium: {
        thin: 16,  // Medium + Thin Crust: $10 + $6 = $16
        thick: 23,  // Medium + Thick Crust: $10 + $13 = $23
        'Gluten-Free': 35  // Medium + Gluten-Free: $10 + $25 = $35
    },
    Large: {
        thin: 26,  // Large + Thin Crust: $20 + $6 = $26
        thick: 33,  // Large + Thick Crust: $20 + $13 = $33
        'Gluten-Free': 45  // Large + Gluten-Free: $20 + $25 = $45
    }
};

// Function to calculate the total price based on selected options
function calculatePrice(size, base) {
    // Retrieve the price from the lookup table based on selected size and base
    return priceLookup[size][base];
}

// Add event listener for each "Add to Cart" button
cartButtons.forEach((button, index) => {
    button.addEventListener('click', function() {
        const selectedItem = {
            name: 'Pizza',  // You can customize this based on your product
            size: sizeSelects[index].value,
            base: baseSelects[index].value,
            price: calculatePrice(sizeSelects[index].value, baseSelects[index].value)
        };

        // Add the selected item to the cartItems array
        cartItems.push(selectedItem);

        // Update the cart items container
        updateCartItems(cartItemsContainer, cartItems);

        // Calculate total price and update the UI
        const totalPrice = calculateTotalPrice(cartItems);
        console.log('Total Price:', totalPrice);
    });
});

// Function to calculate the total price of selected items
function calculateTotalPrice(items) {
    return items.reduce((total, item) => total + item.price, 0);
}

// Function to update the cart items container
function updateCartItems(container, items) {
    container.innerHTML = '';
    items.forEach(item => {
        const cartItemDiv = document.createElement('div');
        cartItemDiv.textContent = `${item.size} ${item.base} - $${item.price}`;
        container.appendChild(cartItemDiv);
    });
}
const imageLookup = {
    small: {
        thin: 'static/small_thin.jpg',
        thick: 'static/small_thick.jpg',
        'Gluten-Free': 'static/small_gluten_free.jpg'
    },
    Medium: {
        thin: 'static/medium_thin.jpg',
        thick: 'static/medium_thick.jpg',
        'Gluten-Free': 'static/medium_gluten_free.jpg'
    },
    Large: {
        thin: 'static/large_thin.jpg',
        thick: 'static/large_thick.jpg',
        'Gluten-Free': 'static/large_gluten_free.jpg'
    }
};
// Function to update the cart items container including images
function updateCartItems(container, items) {
    container.innerHTML = '';
    items.forEach(item => {
        const cartItemDiv = document.createElement('div');
        cartItemDiv.className = 'cart-item'; // Add a class for styling if needed

        const itemImage = document.createElement('img');
        itemImage.src = imageLookup[item.size][item.base]; // Get corresponding image source
        itemImage.alt = `Pizza  `;
        cartItemDiv.appendChild(itemImage);

        const itemDescription = document.createElement('span');
        itemDescription.textContent = `  ${item.size} ${item.base} - $${item.price}`;
        cartItemDiv.appendChild(itemDescription);

        container.appendChild(cartItemDiv);
    });
}
});
// Function to toggle cart container
function toggleCart() {
    const cartContainer = document.querySelector('.cart-container');
    cartContainer.classList.toggle('open');
}