from django.shortcuts import render
from site_app.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'site_app/home.html', {"posts": posts})

# Create your views here.
