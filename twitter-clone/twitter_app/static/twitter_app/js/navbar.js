// DOM element objects
// -------------------
var nav_open_button = document.getElementById("nav_open_btn");
var nav_close_button = document.getElementById('nav_close_btn');
var top_nav_bar = document.getElementById('top-nav-bar');
var logo = document.getElementById('logo');

// EVENTS
// ------

//when the menu is opened :::
document.getElementById("nav_open_btn").onclick = function() {

  // #nav_open_btn
  nav_open_button.style.cssText = 'display:none;'

  // #nav_close_btn
  nav_close_button.style.cssText = 'margin-left: -60px !important; display:block !important;\
  padding:5px !important; background-color: transparent; border: 0px solid \
  transparent; border border: 0px solid transparent; font-size:28px; position:\
  absolute; margin-top: -10px !important; margin-bottom:110px !important; \
  float:right !important;';

  // #top-nav-bar
  top_nav_bar.style.cssText = 'width:100%; height:100vh; transition:0.5s; z-index\
  :1; top:0; left:0; overflow-y:hidden;';

  // #logo
  logo.style.cssText = 'display:none !important;';

  // #home-link
  document.getElementById('home-link').style.cssText = 'color:dimgray; font-we\
  ight: bolder; display:block !important; font-size:25px; margin-bottom:20px !important;\
  width:100%; margin-top:110px!important;';

  // #profile-link
  document.getElementById('profile-link').style.cssText = 'color:dimgray; font-we\
  ight: bolder; display:block !important; font-size:25px; margin-bottom:20px !important;\
  width:100%;';

  // #explore-link
  document.getElementById('explore-link').style.cssText = 'color:dimgray; font-we\
  ight: bolder; display:block !important; font-size:25px; margin-bottom:20px !important;\
  width:100%;';

  // #logout-link
  document.getElementById('logout-link').style.cssText = 'display:block !important;\
  float:left !important; font-weight:bolder; font-size:25px; margin-bottom:20px !important;\
  width:100%; margin-left:0px !important;'

  // #settings-link
  document.getElementById('settings-link').style.cssText = 'display:block !important;\
  float:left !important; font-weight: bolder; font-size:25px; margin-bottom:20px !important;\
  width:100%; margin-left:0px !important;';


}



//when the menu is closed it returns to its first state
document.getElementById('nav_close_btn').onclick = function() {

  // #nav_open_btn
  document.getElementById('nav_open_btn').style.cssText = 'display:inline !important;';

  // #nav_close_btn
  document.getElementById('nav_close_btn').style.cssText = 'display:none !imortant;';

  // #top_nav_bar
  document.getElementById('top-nav-bar').style.cssText = 'overflow-y:hidden !important;\
  width:100%; height:50px; position:fixed; padding:8px 90px 0px 90px !important;\
  background-color:white; borderBottom: 1px solid lightgray; z-index:1; transition:0.5s !important;'

  // #logo
  logo.style.cssText = 'display:inline !important';

  // #home-link
  document.getElementById('home-link').style.cssText = 'display:none !important;'

  // #profile-link
  document.getElementById('profile-link').style.cssText = 'display:none !important;'

  // #explore-link
  document.getElementById('explore-link').style.cssText = 'display:none !important;'

  // #logout-link
  document.getElementById('logout-link').style.cssText = 'display:none !important;'

  // #settings-link
  document.getElementById('settings-link').style.cssText = 'display:none !important;'

}
