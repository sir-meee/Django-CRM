# Generated by Django 3.1.4 on 2021-04-09 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='organisation',
        ),
    ]
