document.addEventListener('DOMContentLoaded', () => {
  const hospital = document.getElementById('hosp_section');

  hospital.addEventListener('submit', (e) => {
    e.preventDefault();
    let reqBody = {};
    Object.keys(hospital.elements).forEach((key) => {
      let element = hospital.elements[key];
      if (element.type !== 'submit') {
        if (element.checked) {
          reqBody[element.name] = element.value;
        }
      }
    });

    window.localStorage.setItem('hospitals', JSON.stringify(reqBody));
    window.location.href = 'cart.html';
  });
});
