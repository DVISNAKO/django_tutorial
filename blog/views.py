from django.shortcuts import render

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 12, 2021'
    }
]

users = [
    {
        'username': 'johndoe',
        },
    {
        'username': 'bob'
        }       
]

def home(request):
    context = {
        'posts': posts,
        'users': users
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
