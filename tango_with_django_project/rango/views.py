from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    about_data = {
        'my_name': 'dj',
        
    }

    return render(request, 'rango/about.html', context=about_data)

def challenge(request):
    challenge_context = {
        'reason': 'because the book said so.',
    }
    return render(request, 'rango/challenge.html', context=challenge_context)
