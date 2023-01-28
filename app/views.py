from django.shortcuts import render
from django.http import HttpResponse
from .forms import VideoForm
from .models import Video

# Create your views here.
def index(request):
    all_video=Video.objects.all()
    if request.method=="POST":
        form=VideoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Uploaded Successfully </h1>")
    else:
        form=VideoForm()
    return render(request,'index.html',{"form":form,"all":all_video})