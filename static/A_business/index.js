// login modal

const login = document.getElementById("login");
login.addEventListener('click', (e) => {
    e.preventDefault();
    const Signup = document.querySelector(".A_business_Signup");
  const varx = document.querySelector(".A_business_login");
  varx.style.display = "block";
  Signup.style.display = "none";

  // Get DOM Elements
  const closeBtn = document.querySelector('.close');
  // // Events
  closeBtn.addEventListener('click', closeModal);
  // Close
  function closeModal() {
    varx.style.display = 'none';
  }
})

// Signup modal
const Signup = document.getElementById("signup");
Signup.addEventListener('click', (e) => {
    e.preventDefault();
  const varx = document.querySelector(".A_business_Signup");
  const login = document.querySelector(".A_business_login");
  varx.style.display = "block";
  login.style.display = "none";

  // Get DOM Elements
  const closeBtn = document.querySelector('.close_Signup');
  // // Events
  closeBtn.addEventListener('click', closeModal);
  // Close
  function closeModal() {
    varx.style.display = 'none';
  }
})

// const Signup_submit = document.querySelector("#signup_submit")
// Signup_submit.addEventListener("click", (e)=>{
//   document.querySelector("#Signup_form").submit();
// })