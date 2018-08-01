from django.shortcuts import render
from django.shortcuts import render_to_response as render
from django.template import RequestContext as ctx
from .forms import PictureForm

# Create your views here.
def index(request):
    if request=="POST":
        form=PictureForm(request.POST,request.FILES)
        if form.is_valid():
            picture=form.save()
    else:
        form=PictureForm()
    return render('home/index.html',locals(), ctx(request))
def enegerOS(request):
    return render('home/enegerOS.html')
def recneger(request):
    return render('home/recneger.html')
def eclokit(request):
    return render('home/eclokit.html')
def contact(request):
    return render('home/contact.html')
