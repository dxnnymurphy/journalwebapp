from django.db import models

# Create your models here.
class journal(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    software = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    class Meta:
        db_table = "journalstable"