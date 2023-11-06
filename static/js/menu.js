document.addEventListener("DOMContentLoaded", function() {
    const sizeDropdownBtns = document.querySelectorAll('.size-dropdown-btn');
    const baseDropdownBtns = document.querySelectorAll('.base-dropdown-btn');
    const sizeDropdownContents = document.querySelectorAll('.size-dropdown-content');
    const baseDropdownContents = document.querySelectorAll('.base-dropdown-content');
    const sizeSelects = document.querySelectorAll('.size-select');
    const baseSelects = document.querySelectorAll('.base-select');
    const cartButtons = document.querySelectorAll('.cart-button');

    // Function to toggle dropdown visibility
    // Function to toggle dropdown visibility with animation
    function toggleDropdown(dropdownContent) {
        // Close other open dropdowns
        sizeDropdownContents.forEach(content => {
            content.classList.remove('show');
        });
        baseDropdownContents.forEach(content => {
            content.classList.remove('show');
        });

        // Toggle dropdown visibility with animation
        dropdownContent.classList.toggle('show');
    }

    // Event listeners for size dropdowns
    sizeDropdownBtns.forEach((button, index) => {
        button.addEventListener('click', function(event) {
            event.stopPropagation();
            toggleDropdown(sizeDropdownContents[index]);
        });
    });

    // Event listeners for base dropdowns
    baseDropdownBtns.forEach((button, index) => {
        button.addEventListener('click', function(event) {
            event.stopPropagation();
            toggleDropdown(baseDropdownContents[index]);
        });
    });

    
});

// Function to toggle cart container
const cartIconBtn = document.querySelector('.cart-icon-btn');
cartIconBtn.addEventListener('click', function() {
    const cartContainer = document.querySelector('.cart-container');
    cartContainer.classList.toggle('open');
});