const hospitals = window.localStorage.getItem('hospitals');

const parsed = JSON.parse(hospitals);

document.addEventListener('DOMContentLoaded', () => {
  const itemsList = document.getElementById('items-list');

  let elements = '<ul class="cart_items">';
  Object.values(parsed).forEach((item) => {
    elements += `<li>${item}</li>`;
  });
  elements += '</ul>';

  console.log('elements', elements);

  itemsList.innerHTML = elements;
});

