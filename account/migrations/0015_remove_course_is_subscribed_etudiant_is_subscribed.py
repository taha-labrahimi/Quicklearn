# Generated by Django 4.2.2 on 2023-07-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_course_is_subscribed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='is_subscribed',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
    ]