# Generated by Django 3.0.8 on 2020-09-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koj', '0001_initial'),
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='lang',
        ),
        migrations.AddField(
            model_name='contest',
            name='lang',
            field=models.ManyToManyField(related_name='contest_language', to='koj.Language'),
        ),
    ]