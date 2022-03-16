from django.db import models

# Create your models here.
class technology(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = "technologies"
    def __str__(self):
        return self.name

class journal(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    technologies = models.JSONField()
    technologiesList = models.JSONField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = "journalstable"
