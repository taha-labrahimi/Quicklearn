# Generated by Django 4.2.1 on 2023-06-26 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.professeur'),
        ),
    ]
