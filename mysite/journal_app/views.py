from re import search
from django.shortcuts import get_object_or_404, render
from journal_app.forms import NewJournalForm
from journal_app.models import journal
from .forms import FilterForm

# Create your views here.
def index(request):
    journals = journal.objects.all()
    search_flag = False
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            for key in form.cleaned_data:
                if key == 'term' and form.cleaned_data[key]:
                    term = form.cleaned_data["term"]
                    journals = journal.objects.filter(title__contains=term)
                    search_flag = True
                if form.cleaned_data[key] is not False and key != 'term':
                    if search_flag == True:
                        journals2 = journal.objects.filter(software__contains=key)
                        journals.union(journals2)
                    else:
                        journals = journal.objects.filter(software__contains=key)
    techform = FilterForm()
    context = {'Journals': journals, 'form': techform}
    return render(request,'journal_app/index.html', context)

def filter(request):
    journals = journal.objects.filter(software='python')
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
    print(entry_dict)
    if request.method == 'POST':
        form = NewJournalForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            if entry_dict["title"] != form.cleaned_data["title"]:
                entry.title = form.cleaned_data["title"]
            if entry_dict["url"] != form.cleaned_data["url"]:
                entry.url = form.cleaned_data["url"]
            if entry_dict["software"] != form.cleaned_data["software"]:
                entry.software = form.cleaned_data["software"]
            if entry_dict["notes"] != form.cleaned_data["notes"]:
                entry.notes = form.cleaned_data["notes"]
            entry.save()
            journals = journal.objects.all()
            return render(request,'journal_app/index.html', {'Journals': journals})
        else: 
            print("not valid")
    return render(request, "journal_app/edit.html", {'entry': entry_dict})

def delete(request, journal_id):
    entry = get_object_or_404(journal, pk=journal_id)
    entry.delete()
    journals = journal.objects.all()
    return render(request,'journal_app/index.html', {'Journals': journals})
