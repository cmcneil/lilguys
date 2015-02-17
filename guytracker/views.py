from guytracker.models import Lilguy, Chapter
from django.http import HttpResponse


def display_guy(request, lilguy_name):
    """ Returns an HttpResponse for an individual lilguy's information \
        and chapters page. """

    # finds all Chapters about lilguy_name
    chapters = (Chapter.objects.select_related()
                .filter(lilguy__name=lilguy_name)
                .order_by('timestamp'))

    lilguy = None
    if len(chapters) > 0:
        lilguy = chapters[0].lilguy
    else:
        return render_to_response('error.html')

    return (render_to_response('display_guy.html', 
                               {'lilguy': lilguy, 'chapters': chapters}))
