from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
    
    <h1>Rango says hey there partner!</h1>
    <a href="/rango/about/">About Page</a>
    
    
    """)

def about(request):
    return HttpResponse("""
    
    
    <h1>Rango says here is the about page.</h1>
    <a href="/">Home</a>

    """)

