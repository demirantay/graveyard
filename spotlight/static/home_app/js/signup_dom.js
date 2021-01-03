office_panel_open_btn = document.getElementById("office-create-button");
office_hidden_panel = document.getElementById("office-hidden-panel");
header = document.getElementById("header");
account_panel_open_btn = document.getElementById("account-create-button");
account_hidden_panel = document.getElementById("account-hidden-panel");

office_panel_open_btn.onclick = function() {
  office_hidden_panel.style.display = "block";
  header.style.marginTop = "40px";
  account_hidden_panel.style.display = "none";
}

account_panel_open_btn.onclick = function() {
  account_hidden_panel.style.display = "block";
  header.style.marginTop = "40px";
  office_hidden_panel.style.display = "none";
}
