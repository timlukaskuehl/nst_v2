from __future__ import print_function
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from django.conf import settings
from nst.forms import IntroForm
from django.core.files.storage import FileSystemStorage
import os
from PIL import Image, ImageOps
from nst.models import UserInput

def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES["user_file"]
        # we don't use a model form, but instead just a file upload field
        file_system = FileSystemStorage()
        # the django API is used in order to save the image onto the hard drive
        file_system.save(uploaded_file.name, uploaded_file)
        img = Image.open(uploaded_file)
        size = (1200, 630)
        img = ImageOps.fit(img, size, Image.ANTIALIAS)
        # we use PIL to resize the image. ANTIALIAS makes sure we keep the 16:9 aspect ratio of the style image
        img.save("D:/Programming/PyTorch_NST_V2/nstapp/nst/user_image/content_resized.jpg")
    return render(request, "upload.html")

def output(request):
    # once the page is requested, the sh script will run and output the final image onto the hard drive
    os.system("D:/Programming/PyTorch_NST_V2/nstapp/nst/run.sh")
    # once the calcululations are done, the website will load
    form = IntroForm()
    posts = UserInput.objects.all()
    args = {"form": form,"posts": posts}
    return render(request, "output.html", args)

class HomeView(TemplateView):
    # creates the home view. Whenever a user wants to access the page, this site shows up
    template_name = "intro.html"

    def get(self, request):
        # sends a get request to show the form on the page
        form = IntroForm()
        return render(request, self.template_name, {"form": form})
        # displays the form on the website

    def post(self, request):
        # sends a post request in order to save the user input to the database
        form = IntroForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data["paintings_name"]
            # cleans the form after data input
            form = IntroForm()
        
        args = {"form": form, "text": text}
        return render(request, self.template_name, args)