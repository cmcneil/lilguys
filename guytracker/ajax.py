from dajaxice.decorators import dajaxice_register
import guytracker.utils as ut
import json
import sys

@dajaxice_register
def auth_lilguy_code(request, url_code, auth_code):
    lilguy_id = ut.urlsafe_code_to_lilguy_id(url_code)
    actual_auth_code = ut.lilguy_id_to_activation_code(lilguy_id)
    # Check to make sure the user hasn't already written a chapter for this guy.
    if request.session.get('has_made_chapter_'+url_code, False):
        return json.dumps({'status': 'ALREADY_WRITTEN'})
    elif auth_code == actual_auth_code:
        return json.dumps({'status': 'VALID'})
    return json.dumps({'status': 'INVALID'})


