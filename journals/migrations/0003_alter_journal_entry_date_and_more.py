# Generated by Django 4.2.11 on 2024-04-26 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0002_remove_journal_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='entry_date',
            field=models.DateField(verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='last_modified_date',
            field=models.DateField(verbose_name='Last modified'),
        ),
    ]