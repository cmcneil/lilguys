from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from guytracker.forms import ChapterForm
from guytracker.models import Lilguy, Chapter
import guytracker.utils as ut

def all_guys(request):
    """
    Give a list of all guys.
    """
    lilguys = Lilguy.objects.all()
    lilguys_to_url_code = {}
    for guy in lilguys:
        lilguys_to_url_code[guy.id] = ut.lilguy_id_to_urlsafe_code(guy.id)
    return render_to_response('all_guys.html', 
                              {'lilguys': lilguys,
                               'lilguys_to_url_code': lilguys_to_url_code})

def display_guy(request, url_code):
    """ Returns an HttpResponse for an individual lilguy's information \
        and chapters page. """
    
    id = ut.urlsafe_code_to_lilguy_id(url_code)
    # finds all Chapters about lilguy_name
    chapters = (Chapter.objects.select_related()
                .filter(lilguy__id=id)
                .order_by('timestamp'))

    lilguy = None
    if len(chapters) > 0:
        lilguy = chapters[0].lilguy
    else:
        return render_to_response('error.html')

    if request.method == 'GET':
        chapter_form = ChapterForm()
    elif request.method == 'POST':
        chapter_form = ChapterForm(request.POST, request.FILES)
        if chapter_form.is_valid():
            new_chapter = chapter_form.save(commit=False)
            new_chapter.lilguy = lilguy
            new_chapter.save()
            return HttpResponseRedirect("/lilguys/" + url_code)
    
    return render_to_response('display_guy.html',
                              {'lilguy': lilguy, 
                               'url_code': url_code,
                               'chapters': chapters,
                               'chapter_form': chapter_form},
                              context_instance=RequestContext(request))
