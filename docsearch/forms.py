from django import forms

class FromName(forms.Form):
    tags = forms.CharField()
    #email = forms.EmailField()
    #text = forms.CharField(widget = forms.Textarea)