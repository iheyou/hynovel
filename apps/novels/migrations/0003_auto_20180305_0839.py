# Generated by Django 2.0.2 on 2018-03-05 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0002_auto_20180305_0834'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Novel',
        ),
    ]
