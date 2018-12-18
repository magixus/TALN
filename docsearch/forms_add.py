from django import forms

ch = ((1,'doc'),(2, 'doc_1'),(3, 'doc_2'),(4, 'doc_3'))

class FromName(forms.Form):
    tag = forms.CharField()
    age = forms.ChoiceField(choices=ch)
    text = forms.CharField(widget = forms.Textarea)