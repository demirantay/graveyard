var search_button = document.getElementById('search-button');
var search_panel = document.getElementById('search_panel');
var close_btn = document.getElementById('search-panel-close');
var search_form = document.getElementById('search_bar');

close_btn.onclick = function() {
  search_panel.style.display = 'none';
}

search_form.onmouseover = function() {
  search_panel.style.display = 'block';
}


/* html of the above search bar in case i lose it
   ==============================================
   <form id="search_bar" action="{% url 'profile' %}" method="GET" accept-charset="utf-8">
     {{ search_form }}
     <button id="search-button" type="submit"><i class="fa fa-search"></i></button>
   </form>
   <!-- hidden search panel -->
   <div id="search_panel">
     <button id="search-panel-close"><i class="fa fa-close"></i></button>
     <br />
     <!-- user cells generated from the search keyword -->
     <div id="search_user_cell">
       <img src="{{ filtered_db_user_settings.profile_photo.url }}" alt="pp" height="50px" style="border-radius:50%;"/>
       <h4><a href="">@{{ filtered_db_user }}</a></h4>
     </div>
   </div>
*/
