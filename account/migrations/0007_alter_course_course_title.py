# Generated by Django 4.2.1 on 2023-06-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_course_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_title',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
