# Generated by Django 4.2.1 on 2023-07-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_rename_response_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_name',
            field=models.CharField(default='test quiz', max_length=255),
        ),
    ]
