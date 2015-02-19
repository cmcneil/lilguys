from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from guytracker.forms import ChapterForm
from guytracker.models import Lilguy, Chapter

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

    if request.method == 'GET':
        chapter_form = ChapterForm()
    
    return render_to_response('display_guy.html',
                              {'lilguy': lilguy, 
                               'chapters': chapters,
                               'chapter_form': chapter_form},
                              context_instance=RequestContext(request))
