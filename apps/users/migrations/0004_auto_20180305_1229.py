# Generated by Django 2.0.2 on 2018-03-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180305_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercollectnovels',
            name='novel_image',
            field=models.ImageField(null=True, upload_to='', verbose_name='小说封面'),
        ),
    ]
