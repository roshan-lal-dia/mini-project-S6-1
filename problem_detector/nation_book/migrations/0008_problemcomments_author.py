# Generated by Django 4.1.5 on 2023-03-12 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nation_book', '0007_problems'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemcomments',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
    ]
