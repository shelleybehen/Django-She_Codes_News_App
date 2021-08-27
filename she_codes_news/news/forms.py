from django import forms
from django.forms import ModelForm
from .models import NewsStory

# Allow Django to infer all the form fields and validation from a model
class StoryForm(ModelForm):
    #nested class we want django to infer from
    class Meta:
        model = NewsStory
        # list of fields to be included in the form
        fields = ['title', 'pub_date', 'content', 'image_url']
        widgets = {'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Selecta date','type':'date'}),
    }

