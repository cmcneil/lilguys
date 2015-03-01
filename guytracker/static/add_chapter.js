jQuery(document).ready( function() {
    $('#code_input').on('input', auth_code_entered_handler);
});

function auth_code_entered_handler() {
    var url_code = $('#url_code').val();
    var auth_code = $(this).val().toUpperCase();
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
    $('#id_code').val($('#code_input').val());
    if (data.status === 'VALID') {
        input_color_to('transparent');
 
        $('#panel-code-input').hide(0, function(){
            $('#add-chapter').slideDown();
            $('html, body').animate({
                scrollTop: ($('#panel-add-chapter').offset().top)
            }, 500);
        });
    } else if (data.status === 'ALREADY_WRITTEN') {
        alert('ALREADY_WRITTEN');
        // Politely tell the user to give other people a chance to write chapters,
        // and if they want to contribute more, go out and find another guy!
        // Don't unhide the form.
    }else {
        // invalid code
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
