# Generated by Django 3.0.8 on 2020-09-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koj', '0003_auto_20200920_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='contest_id',
            field=models.IntegerField(null=True, verbose_name='대회 번호'),
        ),
    ]