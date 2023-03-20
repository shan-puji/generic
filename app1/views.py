from django.shortcuts import render

# Create your views here.
def emoji_world(request):
    return render(request,'emoji_world.html')