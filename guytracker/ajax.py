from dajaxice.decorators import dajaxice_register
import guytracker.utils as ut
import json

@dajaxice_register
def auth_lilguy_code(request, url_code, auth_code):
    lilguy_id = ut.urlsafe_code_to_lilguy_id(url_code)
    actual_auth_code = ut.lilguy_id_to_activation_code(lilguy_id)
    if auth_code == actual_auth_code:
        return json.dumps({'status': 'VALID'})
    return json.dumps({'status': 'INVALID'})


