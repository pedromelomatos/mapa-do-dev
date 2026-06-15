const loginForm = document.querySelector('#loginForm');

loginForm?.addEventListener('submit', (event) => {
  event.preventDefault();
  window.location.href = 'dashboard.html';
});
