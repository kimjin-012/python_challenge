from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def survey(request):
    name_survey = request.POST['name']
    location_survey = request.POST['location']
    language_survey = request.POST['lang']
    comment_survey = request.POST['comment']
    context = {
        'name_survey' : name_survey,
        'location_survey' : location_survey,
        'language_survey' : language_survey,
        'comment survey' : comment_survey
    }
    return render(request, 'show.html',context)
