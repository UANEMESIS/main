# Generated by Django 2.0.5 on 2018-07-07 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zone', '0006_auto_20180708_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreList',
            fields=[
                ('name_of_list', models.CharField(max_length=40)),
                ('num_of_action', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(max_length=300)),
                ('result', models.NullBooleanField()),
                ('comment', models.CharField(blank=True, max_length=300)),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='zone.Author')),
            ],
        ),
        migrations.DeleteModel(
            name='Dota_2',
        ),
    ]
