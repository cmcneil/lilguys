jQuery(document).ready( function() {
    $('#code_input').on('input', auth_code_entered_handler);
    $('#code_input').keyup(
        function (event) {
            if (event.which == 13) {
                auth_code_entered_handler() 
            }
        });
});

function auth_code_entered_handler(event) {
    var url_code = $('#url_code').val();
    var auth_code = $(this).val().toUpperCase();
    // alert('Code is: ' + auth_code);
    if (auth_code.length < 3) {
        input_color_to('transparent');
    }else {
        checking(function() {
            var code_auth_data = {'url_code': url_code,
                                  'auth_code': auth_code};
            Dajaxice.guytracker.auth_lilguy_code(code_validation_callback, code_auth_data);
        });

    }
}

function code_validation_callback(data) {
    if (data.status === 'VALID') {
        $('#id_code').val($('#code_input').val().toUpperCase());
        input_color_to('transparent');
 
        $('#panel-code-input').hide(0, function(){
            $('#add-chapter').slideDown();
            $('html, body').animate({
                scrollTop: ($('#panel-add-chapter').offset().top)
            }, 500);
        });
        create_location_maps_widget('id_map', 'id_found_at_lat', 'id_found_at_lon');
    } else if (data.status === 'ALREADY_WRITTEN') {
        input_color_to('#FFCCDD');
        $('#checking-code').css({'visibility': 'hidden'});
        alert('You have already written a chapter for this guy. Hide it and give someone else a chance!');
        // Politely tell the user to give other people a chance to write chapters,
        // and if they want to contribute more, go out and find another guy!
        // Don't unhide the form.
    }else {
        // invalid codet 
        input_color_to('#FFCCDD');
        $('#checking-code').css({'visibility': 'hidden'});
    }
}

function input_color_to(color) {
    $('#code_input:text').css({  
        'background-color': color
    });
}

function checking(callback) {
    $('#checking-code').css({'visibility': 'visible'});
    if (callback) {
        callback();
    }
}
