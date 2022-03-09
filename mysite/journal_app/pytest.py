import pytest
from django.http import HttpRequest
from .models import journal
from .forms import NewJournalForm
from .views import index, create, edit, delete


def test_journal_model():
    #db_unit_1: tests that the model setup exists and has a suitable schema
    entry = journal()
    assert hasattr(entry, 'title') and hasattr(entry, 'url') and hasattr(entry, 'software') and hasattr(entry, 'notes')

@pytest.mark.django_db
def test_database_access():
    #db_unit_2: tests that the database can be accessed (written to and read from) properly
    entry = journal()
    entry.title = 'test'
    entry.id = 999
    entry.save()
    assert journal.objects.filter(id=999).count() > 0

def test_forms_setup():
    #forms_unit_1: checks that django has defined fields for all html forms required
    form = NewJournalForm()
    assert 'title' and 'url' and 'software' and 'notes' in form.fields

@pytest.mark.django_db
def test_index_view():
    #view_unit_1: tests the default index view returns with an OK http status
    request = HttpRequest()
    result = index(request)
    assert result.status_code == 200

@pytest.mark.django_db
def test_create_view_normal():
    #view_unit_2.1: tests the default index view returns with an OK http status
    request = HttpRequest()
    result = create(request)
    assert result.status_code == 200

@pytest.mark.django_db
def test_create_view_post():
    #view_unit_2.2: tests the default index view returns with an OK http status
    request = HttpRequest()
    request.method = 'POST'
    result = create(request)
    assert result.status_code == 200

@pytest.mark.django_db
def test_edit_view():
    #view_unit_3: tests that after editing an existing view the edit view returns with an OK http status
    request = HttpRequest()
    entry = journal()
    entry.title = 'test'
    entry.id = 999
    entry.save()
    result = edit(request,999)
    assert result.status_code == 200

@pytest.mark.django_db
def test_delete_view():
    #view_unit_4: tests that after creating a journal and deleting the view returns with an OK http status
    request = HttpRequest()
    entry = journal()
    entry.title = 'test'
    entry.id = 999
    entry.save()
    result = delete(request, 999)
    assert result.status_code == 200
    
    


