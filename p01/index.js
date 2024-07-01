// script.js
const loginForm = document.getElementById('login-form');
const userPanel = document.getElementById('user-panel');
const logoutBtn = document.getElementById('logout-btn');
const usernameDisplay = document.getElementById('username-display');

let isLoggedIn = false;

loginForm.addEventListener('submit', (e) => {
	e.preventDefault();
	const username = document.getElementById('username').value;
	const password = document.getElementById('password').value;

	if (username === 'admin' && password === 'password') {
		isLoggedIn = true;
		userPanel.style.display = 'block';
		logoutBtn.style.display = 'block';
		usernameDisplay.textContent = `Bienvenido, ${username}!`;
	} else {
		alert('Nombre de usuario o contrasea incorrectos');
	}
});

logoutBtn.addEventListener('click', () => {
	isLoggedIn = false;
	userPanel.style.display = 'none';
	logoutBtn.style.display = 'none';
	usernameDisplay.textContent = '';
});