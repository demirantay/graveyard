   $(document).ready(function(){
               
                //show button
                $(window).scroll(function() {
                   if ($(this).scrollTop() > 100) {
                       $("#toTheTop").fadeIn(200);
                   } else {
                       $("#toTheTop").fadeOut(200);
                   }
                });
                
                //click event
                $("#toTheTop").click(function(event) {
                    event.preventDefault();
                    $('html, body').animate({scrollTop: 0}, 200);
                    return false;
                });
                
            });