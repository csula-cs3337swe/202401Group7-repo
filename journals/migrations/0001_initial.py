# Generated by Django 4.2.11 on 2024-04-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('journal_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Journal ID')),
                ('user_id', models.IntegerField()),
                ('tag_id', models.CharField()),
                ('title', models.CharField(max_length=200)),
                ('entry_date', models.DateField(verbose_name='date published')),
                ('last_modified_date', models.DateField(verbose_name='last modified')),
                ('content', models.TextField()),
                ('test', models.TextField()),
            ],
        ),
    ]
