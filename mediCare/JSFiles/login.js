document.getElementById('Log-in').addEventListener('click', function (event) {
  event.preventDefault();

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  const formValues = {
    email,
    password,
  };

  function authenticateUser(formValues) {
    return formValues;
  }

  console.log(authenticateUser(formValues));

  const isAuthenticated = authenticateUser(formValues);

  // assume you have a function called "authenticateUser" that returns true if the user is authenticated and false otherwise
  if (isAuthenticated == true) {
    window.location.href = '/index.html';
  } else {
    alert('Invalid user credentials. Please try again.');
  }

  /*  if (password >= 8) {
       window.location.href = '/index.html';
     } else {
       alert('Password should not be less than 8 characters');
     } */
});
