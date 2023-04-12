const image = document.querySelector('.image');
const ambulance = document.querySelector('.services');

image.addEventListener('click', () => {
  ambulance.classList.toggle('list');
});
