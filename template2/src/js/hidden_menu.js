var hidden_menu = document.getElementById("hidden-menu");
var open_hidden_menu_button = document.getElementById("open-hidden-menu-button");
var close_hidden_menu_button = document.getElementById("close-hidden-menu-button");


open_hidden_menu_button.onclick = function() {
  hidden_menu.removeAttribute("style", "display:none;");
  hidden_menu.setAttribute("style", "display:block;");
  /*
    The 'retrn false' below keeps the form from submitting therefore blocks
    the page of reloading. If the page reloads the hidden menu appears for only
    a seconds
  */
  return false;
}

close_hidden_menu_button.onclick = function() {
  hidden_menu.removeAttribute("style", "display:block;");
  hidden_menu.setAttribute("style", "display:none;");
  /*
    The 'retrn false' below keeps the form from submitting therefore blocks
    the page of reloading. If the page reloads the hidden menu appears for only
    a seconds
  */
  return false;
}
