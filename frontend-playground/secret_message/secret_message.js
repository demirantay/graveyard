/*
    Secret Messages

    Desc: I will be implementing few basic ciphers in this module, however
    for starters I am just going to implement ceasers cipher. If I am bored or
    in any need, I will implement the rest of the basic ciphers
*/

"use strict";

// Letter Shift Mechanisms
function shift_letter_forward(key, initial_letter) {
  // the alphabet it expanded in its duplicate in order to avoid `array index
  // out of bounds` once the letters get shifted
  let expanded_alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d",
    "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h",
  ];

  // get the initial index of the letter
  let initial_letter_array_index = expanded_alphabet.indexOf(initial_letter);

  // start shifting the letter with key
  let shifted_letter = expanded_alphabet[initial_letter_array_index + key]

  return shifted_letter;
}

function shift_letter_backwards(key, initial_letter) {
  // the alphabet it expanded in its duplicate in order to avoid `array index
  // out of bounds` once the letters get shifted
  let expanded_alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d",
    "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h",
  ];

  // get the initial index of the letter
  let initial_letter_array_index = expanded_alphabet.indexOf(initial_letter);

  // start shifting the letter backwars with key
  let shifted_letter = expanded_alphabet[initial_letter_array_index - key]

  return shifted_letter;
}


// Encrypt Mechanism
let encrypt_submit_btn = document.getElementById("encode_submit_btn");

function ceaser_cipher_encrypt(event) {
  event.preventDefault(); // prevents btn submitting the form and reloading the page

  // Get input values
  let normal_message = document.getElementById("normal_message").value;
  let shift_key = document.getElementById("encrypt_shift_key").value;
  let encrypted_message = document.getElementById("encrypted_message");

  // Encrypt the message
  let encrypted_message_text = "";
  for (let i = 0; i < normal_message.length; i++) {
    let shifted_letter = shift_letter_forward(Number(shift_key), String(normal_message[i]));
    encrypted_message_text += shifted_letter;
  }

  // return the encrypted value to h1 DOM
  encrypted_message.innerHTML = encrypted_message_text;

}

// Binding the event above to its button
encrypt_submit_btn.addEventListener("click", ceaser_cipher_encrypt);


// Decrypt Mechanism
let decrypt_submit_btn = document.getElementById("decode_submit_btn");

function ceaser_cipher_decrypt(event) {
  event.preventDefault(); // prevents btn submitting the form and reloading the page

  // Get input values
  let encoded_message = document.getElementById("encoded_message").value;
  let shift_key = document.getElementById("decrypt_shift_key").value;
  let decrypted_message = document.getElementById("decrypted_message");

  // Decrypt the message
  let decrypted_message_text = "";
  for (let i = 0; i < encoded_message.length; i++) {
    let shifted_letter = shift_letter_backwards(Number(shift_key), String(encoded_message[i]));
    decrypted_message_text += shifted_letter;
  }

  // return the encrypted value to h1 DOM
  decrypted_message.innerHTML = decrypted_message_text;

}

// Binding the event above to its button
decrypt_submit_btn.addEventListener("click", ceaser_cipher_decrypt);
