# Generated by Django 4.0.3 on 2022-03-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0010_alter_journal_attachment_alter_journal_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='journal',
            name='attachment',
        ),
        migrations.AddField(
            model_name='journal',
            name='technologies',
            field=models.ManyToManyField(to='journal_app.technology'),
        ),
    ]
