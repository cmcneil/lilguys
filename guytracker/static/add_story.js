jQuery(document).ready( function() {
    $("#code-input").on('input', function() {
        console.log('text field code-input changed!');
        Dajaxice.guytracker.auth_lilguy_code(code_validation_callback);
    });
});

function code_validation_callback(response) {
    alert(response.message);
}
