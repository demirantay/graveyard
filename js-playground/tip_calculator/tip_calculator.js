/*

    Project Name: Tip Calculator

    Desc: You enter few questions about the bill and than the program
          outputs you the amount of bill + tip $

    Author: @demirantay (github)

*/


// DOM variables
// ---------------
var calculate_button = document.getElementById("calculate_button");
var amount_you_have_to_pay = document.getElementById("amount_you_have_to_pay");
var bill_amount = document.getElementById("bill_amount");
var service_type = document.getElementById("service_type");
var amount_of_people = document.getElementById("amount_of_people");

// Events
// -----------------

calculate_button.onclick = function() {
  your_share_of_bill = bill_amount.value / amount_of_people.value;

  tip = bill_amount.value * service_type.value;

  amount_you_have_to_pay.innerHTML =  your_share_of_bill + " + tip: " + tip +"$";
}
