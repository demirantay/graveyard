/*
  Module Name: Rock Paper Scissors

  Desc: it is a basic rock paper scissors game implementation on index
*/

"use strict";



// Generate random user selection
function generate_random_user_selection() {}

// Rock Paper Scissor Game

let play_submit_btn = document.getElementById("play_submit_btn");

function rock_paper_scissors(event) {
  event.preventDefault(); // prevents btn submitting the form and reloading the page

  // Get the User Selection
  let user_selection = document.getElementById("user_selection").value;

  // Generate a Random Computer Selection
  let possible_computer_selections = ["rock", "paper", "scissors"];
  let computer_selection = possible_computer_selections[Math.floor(Math.random() * 3)];

  // Change the banners based on the results
  let user_win_status = document.getElementById("user_win_status");
  let user_selected_gesture = document.getElementById("user_selected_gesture");
  let computer_selected_gesture = document.getElementById("computer_selected_gesture");

  if (user_selection === computer_selection) {
    // Tie
    user_win_status.src = "images/tie.png";
    if (user_selection === "rock") {
      user_selected_gesture.src = "images/rock.png";
      computer_selected_gesture.src = "images/rock.png";
    }
    else if (user_selection === "paper") {
      user_selected_gesture.src = "images/paper.png";
      computer_selected_gesture.src = "images/paper.png";
    }
    else if (user_selection === "scissors") {
      user_selected_gesture.src = "images/scissors.png";
      computer_selected_gesture.src = "images/scissors.png";
    }
  }
  else if (user_selection === "rock" && computer_selection === "paper") {
    // lose
    user_win_status.src = "images/lost.png";
    user_selected_gesture.src = "images/rock.png";
    computer_selected_gesture.src = "images/paper.png";
  }
  else if (user_selection === "rock" && computer_selection === "scissors") {
    // win
    user_win_status.src = "images/won.png";
    user_selected_gesture.src = "images/rock.png";
    computer_selected_gesture.src = "images/scissors.png";
  }
  else if (user_selection === "paper" && computer_selection === "scissors") {
    // lose
    user_win_status.src = "images/lost.png";
    user_selected_gesture.src = "images/paper.png";
    computer_selected_gesture.src = "images/scissors.png";
  }
  else if (user_selection === "paper" && computer_selection === "rock") {
    // win
    user_win_status.src = "images/won.png";
    user_selected_gesture.src = "images/paper.png";
    computer_selected_gesture.src = "images/rock.png";
  }
  else if (user_selection === "scissors" && computer_selection === "rock") {
    // lose
    user_win_status.src = "images/lost.png";
    user_selected_gesture.src = "images/scissors.png";
    computer_selected_gesture.src = "images/rock.png";
  }
  else if (user_selection === "scissors" && computer_selection === "paper") {
    // win
    user_win_status.src = "images/won.png";
    user_selected_gesture.src = "images/scissors.png";
    computer_selected_gesture.src = "images/paper.png";
  }

}

// Game Event binding with submit (play) button
play_submit_btn.addEventListener("click", rock_paper_scissors);
