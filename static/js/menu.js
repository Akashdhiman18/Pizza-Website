document.addEventListener("DOMContentLoaded", function() {
    const sizeDropdownBtns = document.querySelectorAll('.size-dropdown-btn');
    const baseDropdownBtns = document.querySelectorAll('.base-dropdown-btn');
    const sizeDropdownContents = document.querySelectorAll('.size-dropdown-content');
    const baseDropdownContents = document.querySelectorAll('.base-dropdown-content');
    const sizeSelects = document.querySelectorAll('.size-select');
    const baseSelects = document.querySelectorAll('.base-select');
    const cartButtons = document.querySelectorAll('.cart-button');

    // Function to toggle dropdown visibility
    function toggleDropdown(dropdownContent) {
        dropdownContent.classList.toggle('show');
    }

    // Event listeners for size dropdowns
    sizeDropdownBtns.forEach((button, index) => {
        button.addEventListener('click', function(event) {
            event.stopPropagation();
            // Close other open dropdowns
            baseDropdownContents.forEach(content => {
                content.classList.remove('show');
            });
            toggleDropdown(sizeDropdownContents[index]);
        });
    });

    // Event listeners for base dropdowns
    baseDropdownBtns.forEach((button, index) => {
        button.addEventListener('click', function(event) {
            event.stopPropagation();
            // Close other open dropdowns
            sizeDropdownContents.forEach(content => {
                content.classList.remove('show');
            });
            toggleDropdown(baseDropdownContents[index]);
        });
    });

    // Add-to-cart functionality
    cartButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            const selectedSize = sizeSelects[index].value;
            const selectedBase = baseSelects[index].value;
            const pizzaName = button.parentNode.parentNode.querySelector('h2').textContent;

            const data = {
                size: selectedSize,
                base: selectedBase,
                pizzaName: pizzaName
            };

            fetch('/add_to_cart', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                console.log(data.message);  // Log the response message
                // You can update the UI or handle the response as needed
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    // Function to toggle cart container
    const cartIconBtn = document.querySelector('.cart-icon-btn');
    cartIconBtn.addEventListener('click', function() {
        const cartContainer = document.querySelector('.cart-container');
        cartContainer.classList.toggle('open');
    });
});
