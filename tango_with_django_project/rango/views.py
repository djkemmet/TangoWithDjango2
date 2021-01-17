from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Create your views here.
def index(request):

    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

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
