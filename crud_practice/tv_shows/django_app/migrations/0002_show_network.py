# Generated by Django 2.2.4 on 2023-02-20 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='network',
            field=models.CharField(default=True, max_length=45),
        ),
    ]