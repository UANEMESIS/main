# Generated by Django 2.0.5 on 2018-07-01 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zone', '0003_auto_20180629_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='author',
            field=models.ManyToManyField(to='zone.Author'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='core_list',
            field=models.ManyToManyField(to='zone.Corelist'),
        ),
    ]
