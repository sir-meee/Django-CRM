# Generated by Django 3.1.4 on 2021-04-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0014_followup'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='converted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]