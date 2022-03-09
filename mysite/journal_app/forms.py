from django import forms

class NewJournalForm(forms.Form):
    title = forms.CharField(label='title', required = True)
    url = forms.CharField(label= 'url', required = False)
    software = forms.CharField(label='software', required = False)
    notes = forms.CharField(label='notes', required=False)
    