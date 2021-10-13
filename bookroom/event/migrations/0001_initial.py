# Generated by Django 3.1.1 on 2021-10-13 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('name', models.CharField(max_length=255, verbose_name='Room Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Event Title')),
                ('all_day', models.BooleanField(default=False, verbose_name='All-Day event')),
                ('start', models.DateTimeField(verbose_name='Event start')),
                ('end', models.DateTimeField(verbose_name='Event end')),
                ('editable', models.BooleanField(default=True, verbose_name='Make the event editable')),
                ('overlap', models.BooleanField(default=True, verbose_name='Make the event overlapping')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
