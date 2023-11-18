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
