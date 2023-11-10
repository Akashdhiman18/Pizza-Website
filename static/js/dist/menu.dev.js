"use strict";

document.addEventListener("DOMContentLoaded", function () {
  var sizeDropdownBtns = document.querySelectorAll('.size-dropdown-btn');
  var baseDropdownBtns = document.querySelectorAll('.base-dropdown-btn');
  var sizeDropdownContents = document.querySelectorAll('.size-dropdown-content');
  var baseDropdownContents = document.querySelectorAll('.base-dropdown-content');
  var sizeSelects = document.querySelectorAll('.size-select');
  var baseSelects = document.querySelectorAll('.base-select');
  var cartButtons = document.querySelectorAll('.cart-button'); // Function to toggle dropdown visibility
  // Function to toggle dropdown visibility with animation

  function toggleDropdown(dropdownContent) {
    // Close other open dropdowns
    sizeDropdownContents.forEach(function (content) {
      content.classList.remove('show');
    });
    baseDropdownContents.forEach(function (content) {
      content.classList.remove('show');
    }); // Toggle dropdown visibility with animation

    dropdownContent.classList.toggle('show');
  } // Event listeners for size dropdowns


  sizeDropdownBtns.forEach(function (button, index) {
    button.addEventListener('click', function (event) {
      event.stopPropagation();
      toggleDropdown(sizeDropdownContents[index]);
    });
  }); // Event listeners for base dropdowns

  baseDropdownBtns.forEach(function (button, index) {
    button.addEventListener('click', function (event) {
      event.stopPropagation();
      toggleDropdown(baseDropdownContents[index]);
    });
  });
}); // Function to toggle cart container

var cartIconBtn = document.querySelector('.cart-icon-btn');
cartIconBtn.addEventListener('click', function () {
  var cartContainer = document.querySelector('.cart-container');
  cartContainer.classList.toggle('open');
});
//# sourceMappingURL=menu.dev.js.map
