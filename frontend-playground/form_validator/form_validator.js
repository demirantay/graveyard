/*
    Form Validation
    ---------------

    Desc: This module validates the form and edits the UI (DOM Elements)
    according to the user credentials. If it is entered wrongly it will
    point out that it is wrong if it is right, it will greet the user.
*/

// User Object
function User(username, password) {
  this.username = String(username);
  this.password = String(password);

  // to string
  this.str = function() {
    return "Username:" + this.username
  };
}

let user_1 = new User("foo", "123");
let user_2 = new User("bar", "123");


// Getting the DOM objects
let warning_banner = document.getElementById("warning_banner");
let login_submit_btn = document.getElementById("login_form_submit_btn");

// Login Form Processing and Its Event bind
function login_form_processing(event) {
  event.preventDefault(); // prevents btn submitting the form and reloading the page

  let username_input = String(document.getElementById("username_input").value);
  let password_input = String(document.getElementById("password_input").value);
  let invalid_credentials = false;

  if (username_input !== user_1.username || password_input !== user_1.password) {
    // the credentials do not match so wrong inputs!
    invalid_credentials = true;
  }
  else if (username_input !== user_2.username || password_input !== user_2.password) {
    // the credentials do not match so wrong inputs!
    invalid_credentials = true;
  }
  else {
    invalid_credentials = false;
  }

  if (invalid_credentials === true) {
    warning_banner.style.display = "block";
  }
  else {
    warning_banner.style.display = "hidden";
  }
}

// event assignments to DOM elements
login_submit_btn.addEventListener("click", login_form_processing);
