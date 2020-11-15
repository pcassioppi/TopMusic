# Generated by Django 3.0.5 on 2020-11-14 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=70)),
                ('plays', models.PositiveIntegerField(default=0)),
                ('artist', models.CharField(default='', max_length=70)),
                ('lfm_link', models.CharField(default='', max_length=70)),
                ('artist_id', models.PositiveIntegerField()),
                ('user', models.CharField(default='', max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=70)),
                ('plays', models.PositiveIntegerField(default=0)),
                ('lfm_link', models.CharField(default='', max_length=70)),
                ('user', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('song_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=70)),
                ('plays', models.PositiveIntegerField(default=0)),
                ('artist', models.CharField(default='', max_length=70)),
                ('lfm_link', models.CharField(default='', max_length=70)),
                ('artist_id', models.PositiveIntegerField()),
                ('user', models.CharField(default='', max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30)),
            ],
        ),
    ]