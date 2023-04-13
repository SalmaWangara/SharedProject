const menu = document.querySelector('.menu-list');
const link = document.querySelector('.nav_link');

menu.addEventListener('click', () => {
  link.classList.toggle('hide');
});
