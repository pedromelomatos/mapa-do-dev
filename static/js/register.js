const registerForm = document.querySelector('#registerForm');

registerForm?.addEventListener('submit', (event) => {
  event.preventDefault();
  window.location.href = registerForm.dataset.loginUrl || '/login';
});
