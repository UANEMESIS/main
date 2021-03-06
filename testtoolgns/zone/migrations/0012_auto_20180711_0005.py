# Generated by Django 2.0.5 on 2018-07-10 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zone', '0011_megaauthor_megachecklist_megasteps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actionz_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doings_2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Author_2',
            fields=[
                ('author_id_2', models.AutoField(primary_key=True, serialize=False)),
                ('author_name_2', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CoreList_2',
            fields=[
                ('name_of_list_2', models.CharField(max_length=40)),
                ('num_of_action_2', models.AutoField(primary_key=True, serialize=False)),
                ('action_2', models.CharField(max_length=300)),
                ('result_2', models.NullBooleanField()),
                ('comment_2', models.CharField(blank=True, max_length=300)),
                ('creator_2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='zone.Author_2')),
            ],
        ),
        migrations.RemoveField(
            model_name='megasteps',
            name='bound_author',
        ),
        migrations.RemoveField(
            model_name='megasteps',
            name='bound_checklist',
        ),
        migrations.DeleteModel(
            name='MegaAuthor',
        ),
        migrations.DeleteModel(
            name='MegaChecklist',
        ),
        migrations.DeleteModel(
            name='MegaSteps',
        ),
        migrations.AddField(
            model_name='actionz_2',
            name='torrent_2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='zone.Author_2'),
        ),
    ]
