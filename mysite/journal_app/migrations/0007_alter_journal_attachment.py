# Generated by Django 4.0.3 on 2022-03-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0006_alter_journal_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='attachment',
            field=models.ImageField(default='.media/White_full.png', upload_to='upload/'),
        ),
    ]
