# Generated by Django 4.0.3 on 2022-03-08 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0002_alter_journal_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='journal',
            table='journalstable',
        ),
    ]
