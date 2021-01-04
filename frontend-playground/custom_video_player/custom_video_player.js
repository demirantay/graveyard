/*
    Module Name: Custom Video Player

    Desc: In this project I tried to create a custom video player with the
    browser supported HTMLvideo API.
*/

"use strict";

// DOM Elements for Video Controls
const video = document.getElementById("video");
const controls = document.getElementById("video_controls");

const play_pause = document.getElementById("play_pause");
const play_stop_icons = document.getElementById("playStopIcons");

const rewind = document.getElementById("rewind");
const forward = document.getElementById("forward");
const timer = document.getElementById("timer");

const full_screen = document.getElementById("full_screen");
const volume = document.getElementById("volume");

// Removing the default controls from js because if the script doesnt load
// there would still be a control
video.removeAttribute("controls");

// DOM mauseover element for the video, if there is a mouse make the controls
// visible if not make it hidden


// Play and Pause Mechanism
play_pause.addEventListener("click", play_pause_video);

function play_pause_video(event) {
  event.preventDefault();

  if (video.paused) {
    video.play();
    play_stop_icons.classList.remove("fa-play");
    play_stop_icons.classList.add("fa-stop");
  }
  else {
    video.pause();
    play_stop_icons.classList.remove("fa-stop");
    play_stop_icons.classList.add("fa-play");
  }
}

// Stopping the Video once it is Finished
video.addEventListener("ended", stop);

function stop() {
  video.pause();
  video.currentTime = 0;
}

// Rewind Mechanism
rewind.addEventListener("click", rewind_video);

function rewind_video(event) {
  event.preventDefault();

  video.currentTime -= 3;
}


// Forward Mechanism
forward.addEventListener("click", forward_video);

function forward_video(event) {
  event.preventDefault();

  video.currentTime += 3;
}


// Timer Mechanism
video.ontimeupdate = function() { update_time() };

function update_time() {
  timer.innerHTML = video.currentTime.toFixed(2);
}



// Full Screen Mechanism
full_screen.addEventListener("click", full_screen_video);

function full_screen_video(event) {
  event.preventDefault();

  alert("Its easy to implement it but I am just bored so nope, maybe later.");
}


// Volume Mechanism
volume.addEventListener("click", volume_video);

function volume_video(event) {
  event.preventDefault();

  alert("Its easy to implement it but I am just bored so nope, maybe later.");
}
