/*
    Module Name: Tip Calculator

    Desc: Tip calculator and a cost splitter for a restaurant check bill. This
    is meant to be extremly simple, i dont even know why i am coding this. But
    still it was in the project list of the article and iwanted to create
    every project on it.
*/

let tip_calculate_btn = document.getElementById("tip_calculator_submit_btn");

// Calculate tip and bill
function tip_calculate(event) {
  event.preventDefault(); // prevents btn submitting the form and reloading the page

  // Get the input values
  let total_cost = document.getElementById("total_cost").value;
  let people_amount = document.getElementById("people_amount").value;
  let service_quality = document.getElementById("service_quality").value;

  // Calculate and print the cost-for-each-person
  let cost = total_cost / people_amount;
  document.getElementById("each_person_cost").innerHTML = cost;

  // Calculate and print the tip you will pay
  if (service_quality === "excellent") {
    let tip = cost * 0.20;
    document.getElementById("tip_you_will_pay").innerHTML = tip;
  }
  else if (service_quality === "normal") {
    let tip = cost * 0.10;
    document.getElementById("tip_you_will_pay").innerHTML = tip;
  }
  else if (service_quality === "bad") {
    let tip = cost * 0.05;
    document.getElementById("tip_you_will_pay").innerHTML = tip;
  }
  else {
    let tip = cost * 0.01;
    document.getElementById("tip_you_will_pay").innerHTML = tip;
  }

}

// Binding the event above to its button
tip_calculate_btn.addEventListener("click", tip_calculate);
