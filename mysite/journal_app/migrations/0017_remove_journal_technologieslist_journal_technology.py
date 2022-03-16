# Generated by Django 4.0.3 on 2022-03-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0016_alter_journal_technologieslist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='technologiesList',
        ),
        migrations.AddField(
            model_name='journal',
            name='technology',
            field=models.ManyToManyField(to='journal_app.technology'),
        ),
    ]
