# Generated by Django 4.0.3 on 2022-03-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0011_technology_remove_journal_attachment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='technologies',
        ),
        migrations.AddField(
            model_name='journal',
            name='technologies',
            field=models.CharField(default='no', max_length=100),
            preserve_default=False,
        ),
    ]