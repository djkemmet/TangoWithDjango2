from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from rango.models import Category, Page 
from rango.forms import CategoryForm, PageForm

# Create your views here.
def index(request):

    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = Page.objects.order_by('-views')[:5]

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


def show_category(request, category_name_slug):
    context_dict = {}

    try:

        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['page'] = None

    return render(request, 'rango/category.html', context=context_dict)


def add_category(request):
    form = CategoryForm()

    # If we are POST-ing to the URL associated with this view...
    if request.method == 'POST':
        
        # Create a new instance of the CategoryForm class from the data in our request body.
        form = CategoryForm(request.POST)

        # if the form passes all validation checks
        if form.is_valid():

            # Save the form and commit it to the database.
            form.save(commit=True)

            return redirect('/rango/')

        else:
            print(form.errors)

        
        
    # Implicit Else, if we're not posting, return the rendered template. 
    return render(request, 'rango/add_category.html', {'form': form})

        
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    # You cannot add a page to a Category that does not exist...
    if category is None:
        return redirect('/rango/')
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('rango:show_category',
                kwargs={'category_name_slug':
                category_name_slug}))
            else:
                print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)