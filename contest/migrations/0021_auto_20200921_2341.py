# Generated by Django 3.0.8 on 2020-09-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0020_auto_20200921_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conproblem',
            name='id',
        ),
        migrations.AddField(
            model_name='conproblem',
            name='conp_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
