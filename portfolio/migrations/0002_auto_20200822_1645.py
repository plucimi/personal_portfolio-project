# Generated by Django 3.0.3 on 2020-08-22 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='ufl',
            new_name='url',
        ),
    ]