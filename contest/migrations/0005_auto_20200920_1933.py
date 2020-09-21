# Generated by Django 3.0.8 on 2020-09-20 10:33

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_contest_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='lang',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('0', 'C'), ('1', 'C++'), ('2', 'Java'), ('3', 'Python')], max_length=7),
        ),
    ]