'use strict';

//=====================================
//DOM elements

//session buttons
var pomodoro_button = document.getElementById('pomodoro-button');
var short_button = document.getElementById('short-button');
var long_button = document.getElementById('long-button');
//Clock
var clock = document.getElementById('clock');
//decision buttons
var reset_button = document.getElementById('reset-button');
var faq_button = document.getElementById('faq_button');
var settings_button = document.getElementById('settings_button');


// Functions

//boot session it stars a countdown and is able to stop a session once it has a
//new session request.

var count_down;

var boot_session = function(initial_minutes, initial_seconds) {
  var minutes = initial_minutes;
  var seconds = initial_seconds;
  clock.innerHTML = minutes + ':' + seconds;
  count_down = setInterval(function() {
    seconds--;
    if (seconds == 0) {
      minutes--;
      if (minutes > 0) {
        seconds = 60;
      }
    }
    clock.innerHTML = minutes + ':' + seconds;
    if ( seconds == 0) {
      clearInterval(count_down);
    }
  }, 1000);
}

var kill_session = function() {
  clearInterval(count_down);
}


//MAIN PROGRAM LOGIC
//===================


// 1) - I can click on the pomodoro button and a 25 min session starts.
pomodoro_button.onclick = function() {
  kill_session();
  boot_session(24, 60);
}

// 2) I can click short button and the timer starts a 5 min session
short_button.onclick = function() {
  kill_session();
  boot_session(4, 60);
}

// 3) I can click long button and timer starts a long session.
long_button.onclick = function() {
  kill_session();
  boot_session(19, 60);
}

// 4) There is a reset button that resets the timer
reset_button.onclick = function() {
  kill_session();
  clock.innerHTML = '25:00';
}

/*

  Stroing the code because I will add more features later on such as start, stop
  and a settings button.

  Q. Why not use git?
  A. The main logic is only 50 lines so I want to be able to quickly edit it in
      the future without having to toggle between terminal and atom.



  CODE
  -------------

  'use strict';

  //=====================================
  //DOM elements

  //session buttons
  var pomodoro_button = document.getElementById('pomodoro-button');
  var short_button = document.getElementById('short-button');
  var long_button = document.getElementById('long-button');
  //Clock
  var clock = document.getElementById('clock');
  //decision buttons
  var reset_button = document.getElementById('reset-button');
  var faq_button = document.getElementById('faq_button');
  var settings_button = document.getElementById('settings_button');


  // Functions

  //boot session it stars a countdown and is able to stop a session once it has a
  //new session request.

  var count_down;

  var boot_session = function(initial_minutes, initial_seconds) {
    var minutes = initial_minutes;
    var seconds = initial_seconds;
    clock.innerHTML = minutes + ':' + seconds;
    count_down = setInterval(function() {
      seconds--;
      if (seconds == 0) {
        minutes--;
        if (minutes > 0) {
          seconds = 60;
        }
      }
      clock.innerHTML = minutes + ':' + seconds;
      if ( seconds == 0) {
        clearInterval(count_down);
      }
    }, 1000);
  }

  var kill_session = function() {
    clearInterval(count_down);
  }


  //MAIN PROGRAM LOGIC
  //===================


  // 1) - I can click on the pomodoro button and a 25 min session starts.
  pomodoro_button.onclick = function() {
    kill_session();
    boot_session(24, 60);
  }

  // 2) I can click short button and the timer starts a 5 min session
  short_button.onclick = function() {
    kill_session();
    boot_session(4, 60);
  }

  // 3) I can click long button and timer starts a long session.
  long_button.onclick = function() {
    kill_session();
    boot_session(19, 60);
  }

  // 4) There is a reset button that resets the timer
  reset_button.onclick = function() {
    kill_session();
    clock.innerHTML = '25:00';
  }

  // 5) There is a settings button that lets you cahnge the time of the timers
  settings_button.onclick = function() {

  }








*/
