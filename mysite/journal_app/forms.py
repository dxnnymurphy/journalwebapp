from django import forms

class NewJournalForm(forms.Form):
    title = forms.CharField(label='title', required = True)
    url = forms.CharField(label= 'url', required = False)
    software = forms.CharField(label='software', required = False)
    notes = forms.CharField(label='notes', required=False)
    file = forms.ImageField(label='file', required=False)

class FilterForm(forms.Form):
    term = forms.CharField(label='term', required = False)
    python = forms.BooleanField(required=False)
    django = forms.BooleanField(required=False)
    html = forms.BooleanField(required=False)
    css = forms.BooleanField(required=False)

    