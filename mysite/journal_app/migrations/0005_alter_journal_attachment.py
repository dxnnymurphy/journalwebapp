# Generated by Django 4.0.3 on 2022-03-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0004_journal_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='attachment',
            field=models.ImageField(default='mysite/journal_app/media/White_full.png', upload_to='upload/'),
        ),
    ]