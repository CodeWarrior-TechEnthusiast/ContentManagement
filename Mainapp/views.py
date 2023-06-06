from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .models import WriteaBlog

def welcome(request):
    fin = WriteaBlog.objects.all()
    return render(request, 'home.html', context={'fin': fin})

def contact(request):
    return render(request, 'contact.html')

def help(request):
    return render(request, 'help.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect("/login")
    else:
        form = UserCreationForm()
    return render(request, 'Signup.html', context = {'form': form})

@login_required(login_url='login')
def writeablog(request):
    if request.method == "POST":
        main_form = BlogForm(request.POST, request.FILES)
        if main_form.is_valid():
            main_form.save()
            return HttpResponseRedirect("/")
        else:
            print("Hi")
            return HttpResponseRedirect("/")
    else:
        main_form = BlogForm()
    return render(request=request, template_name="blog-editor.html", context = {'main_form': main_form})