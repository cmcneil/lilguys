jQuery(document).ready( function() {
    $('#code_input').on('input', auth_code_entered_handler);
});

function auth_code_entered_handler() {
    var url_code = $('#url_code').val();
    var auth_code = $(this).val();
    if (auth_code.length >= 3) {
        var code_auth_data = {'url_code': url_code,
                              'auth_code': auth_code};
        Dajaxice.guytracker.auth_lilguy_code(code_validation_callback, code_auth_data);
    }
}

function code_validation_callback(data) {
    $('#id_code').val($('#code_input').val());
    if (data.status === 'VALID') {
        alert('VALID');
        // Unhide form
    } else if (data.status === 'ALREADY_WRITTEN') {
        alert('ALREADY_WRITTEN');
        // Politely tell the user to give other people a chance to write chapters,
        // and if they want to contribute more, go out and find another guy!
        // Don't unhide the form.
    }else {
        alert('INVALID');
        // Print message saying that code is invalid(lil red text underneath field?).
    }
}
