# Generated by Django 3.2.5 on 2021-09-04 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_alter_project_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-pk']},
        ),
    ]
