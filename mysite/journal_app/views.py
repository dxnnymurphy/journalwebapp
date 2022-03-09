from django.shortcuts import get_object_or_404, render
from journal_app.forms import NewJournalForm
from journal_app.models import journal

# Create your views here.
def index(request):
    journals = journal.objects.all()
    return render(request,'journal_app/index.html', {'Journals': journals})

def create(request):
    if request.method == 'POST':
        form = NewJournalForm(request.POST or None)
        if form.is_valid():
            entry = journal()
            entry.title = form.cleaned_data["title"]
            entry.url = form.cleaned_data["url"]
            entry.software = form.cleaned_data["software"]
            entry.notes = form.cleaned_data["notes"]
            entry.save()
            journals = journal.objects.all()
            return render(request,'journal_app/index.html', {'Journals': journals})
        else:
            return render(request, "journal_app/create.html")
    return render(request, "journal_app/create.html")


def edit(request, journal_id):
    entry = get_object_or_404(journal, pk=journal_id)
    entry_dict = entry.__dict__
    form = NewJournalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if entry_dict["title"] != form.cleaned_data["title"]:
                entry.title = form.cleaned_data["title"]
            if entry_dict["url"] != form.cleaned_data["url"]:
                entry.title = form.cleaned_data["url"]
            if entry_dict["software"] != form.cleaned_data["software"]:
                entry.title = form.cleaned_data["software"]
            if entry_dict["notes"] != form.cleaned_data["notes"]:
                entry.title = form.cleaned_data["notes"]
            entry.save()
            journals = journal.objects.all()
            return render(request,'journal_app/index.html', {'Journals': journals})
    return render(request, "journal_app/edit.html", {'entry': entry_dict})

def delete(request, journal_id):
    entry = get_object_or_404(journal, pk=journal_id)
    entry.delete()
    journals = journal.objects.all()
    return render(request,'journal_app/index.html', {'Journals': journals})
