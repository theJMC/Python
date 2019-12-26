from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'JamesMcC',
        'title': 'First Post',
        'content': 'First Post Content',
        'date_posted': "Now"
    },
    {
        'author': 'TheJMC',
        'title': '2nd Post',
        'content': 'Second Post Content',
        'date_posted': "Now + 1"
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)