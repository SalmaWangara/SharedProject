document
  .getElementById('sign-up')
  .addEventListener('click', function (event) {
    event.preventDefault();

    var firstname = document.getElementById('first-name').value;
    var lastname = document.getElementById('last-name').value;
    var dob = document.getElementById('date-of-birth').value;
    var location = document.getElementById('location').value;
    var email = document.getElementById('email').value;
    var contact = document.getElementById('phone-number').value;
    var password = document.getElementById('password').value;

    const formValues = {
      firstname,
      lastname,
      dob,
      location,
      email,
      contact,
      password,
    };

    function authenticateUser(formValues){
      return formValues;                                       
    }

    /* console.log(authenticateUser(formValues)); */

    // const values = [1, 2, 3, 4, 5, 6, 7]
    // const [one, two, three, ...nums ] = values;

    // const myObjectValues = { firstname: '', lastname: '' }
    // const myObject = { ...myObjectValues, ...otherValues, firstname: 'New name', }

    const isAuthenticated = authenticateUser(formValues);

    /* console.log('isAuthenticated', isAuthenticated); */

    if (isAuthenticated) {
      window.location.href = 'index.html';
    } else {
      alert('Invalid user credentials. Please try again.');
    }
  });
