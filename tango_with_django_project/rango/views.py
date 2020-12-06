from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("""
    
    
    <h1>Rango says here is the about page.</h1>
    <a href="/">Home</a>

    """)

