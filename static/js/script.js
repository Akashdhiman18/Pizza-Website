let navbar = document.querySelector('.header .flex .navbar');

const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");
signupBtn.onclick = (()=>{
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";
});
loginBtn.onclick = (()=>{
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";
});
signupLink.onclick = (()=>{
  signupBtn.click();
  return false;
});

function openForm() {
  var wrapper = document.querySelector('.wrapper');
  wrapper.style.display = (wrapper.style.display === 'none' || wrapper.style.display === '') ? 'block' : 'none';
}
const deliveryText = document.querySelector(".title-text .delivery");
      const deliveryForm = document.querySelector("form.delivery");
      const deliveryBtn = document.querySelector("label.delivery");
      const takeawayBtn = document.querySelector("label.takeaway");
      const takeawayLink = document.querySelector("form .takeaway-link a");
      takeawayBtn.onclick = (()=>{
        deliveryForm.style.marginLeft = "-50%";
        deliveryText.style.marginLeft = "-50%";
      });
      deliveryBtn.onclick = (()=>{
        deliveryForm.style.marginLeft = "0%";
        deliveryText.style.marginLeft = "0%";
      });
      takeawayLink.onclick = (()=>{
        takeawayBtn.click();
        return false;
      });
