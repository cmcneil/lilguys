from dajaxice.decorators import dajaxice_register
from django.utils import json

@dajaxice_register
def auth_lilguy_code(request):
    return json.dumps({'message': 'Hello!'})


