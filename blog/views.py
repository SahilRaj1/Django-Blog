from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Sahil Raj',
        'title': 'Jod Blog',
        'content': 'My name is Sahil Raj',
        'date_posted': 'September 27, 2021'
    },
    {
        'author': 'Ritika Jagtap',
        'title': 'Noob Blog',
        'content': 'My name is Ritika Jagtap',
        'date_posted': 'October 17, 2021'
    }
]

# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

