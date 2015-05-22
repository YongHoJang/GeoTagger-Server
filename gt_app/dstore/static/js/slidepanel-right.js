var dataStr = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \
        Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, \
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. \
        It has survived not only five centuries, but also the leap into electronic typesetting, \
        Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, \
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. \
        It has survived not only five centuries, but also the leap into electronic typesetting, \
        Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, \
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. \
        It has survived not only five centuries, but also the leap into electronic typesetting, \
        Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, \
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. \
        It has survived not only five centuries, but also the leap into electronic typesetting, \
        Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, \
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. \
        It has survived not only five centuries, but also the leap into electronic typesetting, \
        remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets"

$(document).ready(function(){
    $("#navigation li a").on("click", function(e){
        e.preventDefault();
        var hrefval = $(this).attr("href");

        if(hrefval == "#panel") {
            var distance = $('#main-content').css('right');

            if(distance == "auto" || distance == "0px") {
                $(this).addClass("open");
                
                openSidePanel();
            } else {
                closeSidePanel();
            }
        }
    }); // end click event handler
  
  
    $("#closebtn").on("click", function(e){
        e.preventDefault();
        closeSidePanel();
    }); // end close button event handler

    function openSidePanel() {
        $('#main-content').animate(
            {
                right: '400px'
            }, 
            400, 
            'easeOutQuint'
        ); 
        $('#panel-button').html('close&nbsp;&raquo;');
        $('#panel').text(dataStr);
        /*
        $('#panel-button').animate(
            {
                right: "-= 400";    
            },
            400,
            'easeOutQuint'
        );
        */

    }
  
    function closeSidePanel(){
        $("#navigation li a").removeClass("open");
        $('#main-content').animate({
        right: '0px'
        }, 400, 'easeOutQuint');
        $('#panel-button').html('&laquo;&nbsp;open');
        $('#panel').text('');
    }
}); 