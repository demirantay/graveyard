/*
  Module Name: UI Design Editor

  Desc: This small frontend program lets users edit the design of html elements
        with forms dynamically without touching the code. The program will ou-
        -tput the neccessary css code for the selected styles.
*/

let ui_design_run_btn = document.getElementById("ui_design_submit_btn");

// ui design preview event form
function ui_design_preview(event) {
  event.preventDefault(); // prevents btn submitting the form and reloading the page

  // Get the neccessary info from the selected form DOM
  let btn = document.getElementById("button_element");
  let btn_color = document.getElementById("colors").value;
  let btn_type = document.getElementById("type").value;

  // Update Button Color
  if (btn_color === "red") {
    btn.classList.add("red_color");
  }
  else if (btn_color === "purple") {
    btn.classList.add("purple_color");
  }
  else if (btn_color === "blue") {
    btn.classList.add("blue_color");
  }
  else if (btn_color === "green") {
    btn.classList.add("green_color");
  }
  else if (btn_color === "yellow") {
    btn.classList.add("yellow_color");
  }
  else if (btn_color === "orange") {
    btn.classList.add("orange_color");
  }
  else if (btn_color === "grey") {
    btn.classList.add("grey_color");
  }
  else if (btn_color === "navy") {
    btn.classList.add("navy_color");
  }
  else if (btn_color === "black") {
    btn.classList.add("black_color");
  }

  // Update Button Type
  if (btn_type === "normal_type") {
    btn.classList.add("normal_type");
  }
  else if (btn_type === "hard_borders_type") {
    btn.classList.add("hard_borders_type");
  }


  // Update the code preview
  // color update
  let color_code_snippet = document.getElementById("color_code_snippet");

  if (btn_color === "red") {
    let css_code = "\n\tcolor: white;\n\tbackground-color: #E74C3C;";
    color_code_snippet.innerHTML = css_code;
  }
  else if (btn_color === "purple") {
    let css_code = "\n\tcolor: white;\n\tbackground-color: #9B59B6;";
    color_code_snippet.innerHTML = css_code;
  }
  else if (btn_color === "blue") {
    let css_code = "\n\tcolor: white;\n\tbackground-color: #3498DB;";
    color_code_snippet.innerHTML = css_code;
  }
  else if (btn_color === "green") {
    let css_code = "\n\tcolor: white;\n\tbackground-color: #27AE60;";
    color_code_snippet.innerHTML = css_code;
  }
  else if (btn_color === "yellow") {
    let css_code = "\n\tcolor: white;\n\tbackground-color: #F1C40F;";
    color_code_snippet.innerHTML = css_code;
  }
  else if (btn_color === "orange") {
    let css_code = "\n\tcolor: white;\n\tbackground-color: #F39C12;";
    color_code_snippet.innerHTML = css_code;
  }
  else if (btn_color === "grey") {
    let css_code = "\n\tcolor: white;\n\tbackground-color: #7F8C8D;";
    color_code_snippet.innerHTML = css_code;
  }
  else if (btn_color === "navy") {
    let css_code = "\n\tcolor: white;\n\tbackground-color: #2C3E50;";
    color_code_snippet.innerHTML = css_code;
  }
  else if (btn_color === "black") {
    let css_code = "\n\tcolor: white;\n\tbackground-color: #2C3E50;";
    color_code_snippet.innerHTML = css_code;
  }

  // style update
  let type_code_snippet = document.getElementById("type_code_snippet");

  if (btn_type === "normal_type") {
    let css_code = "\n\tborder-radius: 10px; \n\tpadding: 4px 18px;\
    \n\tborder: 1px solid transparent;";
    type_code_snippet.innerHTML = css_code;
  }
  else if (btn_type === "hard_borders_type") {
    let css_code = "\n\tborder-radius: 10px; \n\tpadding: 4px 18px;\
    \n\tborder: 3px solid black;";
    type_code_snippet.innerHTML = css_code;
  }

}

// event binds to the elements
ui_design_run_btn.addEventListener("click", ui_design_preview);
