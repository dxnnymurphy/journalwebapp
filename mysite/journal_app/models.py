from django.db import models

# Create your models here.
class journal(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    software = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    attachment = models.ImageField(upload_to='upload/', default='default.png')
    class Meta:
        db_table = "journalstable"