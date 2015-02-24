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
    lilguy_url_code_to_name = {}
    for guy in lilguys:
        lilguy_url_code_to_name[ut.lilguy_id_to_urlsafe_code(guy.id)] = guy.name
    return render_to_response('all_guys.html', 
                              {'lilguy_url_code_to_name': lilguy_url_code_to_name})

def display_guy(request, url_code):
    """ Returns an HttpResponse for an individual lilguy's information \
        and chapters page. """
    print url_code + "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    # If the param is empty, send them the all_guys page instead.
    if not url_code:
        return all_guys(request)

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
