from django.shortcuts import render
from journal_app.forms import NewJournalForm
from journal_app.models import journal

# Create your views here.
def index(request):
    journals = journal.objects.all()
    return render(request,'journal_app/index.html', {'Journals': journals})

def create(request):
    form = NewJournalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            entry = journal()
            entry.title = form.cleaned_data["title"]
            entry.url = form.cleaned_data.get("url")
            entry.software = form.cleaned_data["software"]
            entry.notes = form.cleaned_data["notes"]
            entry.save()
            journals = journal.objects.all()
            return render(request,'journal_app/index.html', {'Journals': journals})
        else:
            return render(request, "journal_app/create.html")
    return render(request, "journal_app/create.html")

#not currently working
def edit(request):

    form = NewJournalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            return render(request)