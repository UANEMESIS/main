# Generated by Django 2.0.5 on 2018-06-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('num_of_checklist', models.AutoField(primary_key=True, serialize=False)),
                ('name_of_checklist', models.CharField(max_length=80)),
                ('date_of_checklist_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Corelist',
            fields=[
                ('num_of_action', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(max_length=300)),
                ('result', models.NullBooleanField()),
                ('comment', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]