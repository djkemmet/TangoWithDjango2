from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):

    # Define the fields of our form.
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # Provides additional information about the form. 
    class Meta:

        # This form is linked to the Category model.
        model = Category

        # Just show the name field.
        fields = ('name',)

    
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page

        #hide the Fkey
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('https://'):
            url = f'https://{url}'
            cleaned_data['url'] = url

        return cleaned_data
