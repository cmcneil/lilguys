from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from guytracker.forms import ChapterForm
import guytracker.messages as msg
from guytracker.models import Lilguy, Chapter
import guytracker.utils as ut
import json

def all_guys(request):
    """
    Give a list of all guys.
    """
    lilguys = Lilguy.objects.all()
    lilguy_url_code_to_name = {}
    for guy in lilguys:
        lilguy_url_code_to_name[ut.lilguy_id_to_urlsafe_code(guy.id)] = guy.name
   
    print ut.lilguys_to_JS(lilguys)
    # Make a list of all the gps coordinates.
    lilguy_coords = json.dumps(
        map(lambda c: {'lat': c.current_lat, 'lng': c.current_lon}, lilguys))
    return render_to_response('all_guys.html', 
                              {'lilguy_url_code_to_name': lilguy_url_code_to_name,
                               'lilguy_coords': lilguy_coords},
                              context_instance=RequestContext(request))

def display_guy(request, url_code):
    """ Returns an HttpResponse for an individual lilguy's information \
        and chapters page. """
    # If the param is empty, send them the all_guys page instead.
    if not url_code:
        return all_guys(request)

    id = ut.urlsafe_code_to_lilguy_id(url_code)
    secret_code = ut.lilguy_id_to_activation_code(id)

    print "id: " + str(id) + ", url_code: " + url_code + ", secret_code: " + secret_code
    lilguy = Lilguy.objects.get(id=id)    
    # finds all Chapters about lilguy_name
    chapters = (Chapter.objects.select_related()
                .filter(lilguy=lilguy)
                .order_by('timestamp'))

    if request.method == 'GET':
        chapter_form = ChapterForm()
    elif request.method == 'POST':
        if request.session.get('has_made_chapter_'+url_code, False):
            return render_to_response('error.html', 
                                      {'error_code': '403',
                                       'error_explanation': 
                                         msg.ERR_ALREADY_WRITTEN_EXPL},
                                       context_instance=RequestContext(request))
        chapter_form = ChapterForm(request.POST, request.FILES)
        if chapter_form.cleaned_data['code'] != secret_code:
            return render_to_response('error.html',
                                      {'error_code': '401',
                                       'error_explanation': msg.ERR_WRONG_CODE_EXPL},
                                       context_instance=RequestContext(request))
        if chapter_form.is_valid():
            new_chapter = chapter_form.save(commit=False)
            new_chapter.lilguy = lilguy
            new_chapter.save()
            # Update the guy's location in the DB
            lilguy.current_lat = new_chapter.found_at_lat
            lilguy.current_lon = new_chapter.found_at_lon
            lilguy.save()
            request.session['has_made_chapter_'+url_code] = True
            return HttpResponseRedirect("/lilguys/" + "g/" + url_code)
        else:
            print "form errors: " + str(chapter_form.errors)

    # Make a list of all the gps coordinates.
    journey_coords = json.dumps(
            map(lambda c: {'lat': c.found_at_lat, 'lng': c.found_at_lon}, chapters))
    return render_to_response('display_guy.html',
                              {'lilguy': lilguy, 
                               'url_code': url_code,
                               'chapters': chapters,
                               'journey_coords': journey_coords,
                               'chapter_form': chapter_form},
                               context_instance=RequestContext(request))
