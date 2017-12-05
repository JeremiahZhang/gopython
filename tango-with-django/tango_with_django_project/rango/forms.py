from django import forms

from rango.models import Page
from rango.models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name', )

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # We can either exclude the category field from the form.
        exclude = ('category', )
        # Or specify the field to include (i.e. not include the category field)
        # field = ('title', 'url', 'views')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        # IF url is not empty and does not start with "http://",
        # then prepend 'http://'
        if url and not url.startwith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            
            return cleaned_data